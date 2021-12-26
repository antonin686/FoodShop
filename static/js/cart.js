window.onload = () => {
  cartInit();
  getCartDetails();
  function cartInit() {
    let orderbtns = document.querySelectorAll(".btn-order");
    orderbtns.forEach((btn) => {
      btn.addEventListener("click", (event) => {
        let id = event.target.id.split("-")[2];
        let quantity = document.querySelector(`#quantity-${id}`).value;
        let formData = new FormData();
        formData.append("product_id", id);
        formData.append("quantity", quantity);
        fetchPost(urls.addToCart, formData).then((response) => {
          if (response == "success") {
            getCartDetails().then(() => {
              alertify.success("Order has been placed");
            });
          }
        });
      });
    });
  }

  async function updateCart(event) {
    let el = event.target;
    let id = el.id.split("-")[1];
    let price = el.id.split("-")[2];
    let cartItemTotalEl = document.querySelector(`#cartItemTotal-${id}`);
    let cartTotalEl = document.querySelector(`#cartTotal`);
    let quantity = el.value;
    let oldCartItemTotal = parseFloat(cartItemTotalEl.innerHTML);
    let oldCartTotal = parseFloat(cartTotalEl.innerHTML);
    let newCartItemTotal = quantity * price;
    let newCartTotal = oldCartTotal + (newCartItemTotal - oldCartItemTotal);
    
    cartItemTotalEl.innerHTML = newCartItemTotal.toFixed(2);
    cartTotalEl.innerHTML = newCartTotal.toFixed(2);

    let formData = new FormData();
    formData.append("cartitem_id", id);
    formData.append("quantity", quantity);

    let res = await fetchPost(urls.updateCart, formData);

    if (res == "success") {
      updateCartCount();
    }
  }

  async function updateCartCount() {
    let data = await fetchGet(urls.getCartDetails);
    let counterEl = document.querySelector("#cart-counter");

    counterEl.innerHTML = data.count;
  }

  async function removeCart(event) {
    let el = event.currentTarget;
    let id = el.id.split("-")[1];
    let formData = new FormData();
    formData.append("cartitem_id", id);
    let res = await fetchPost(urls.deleteCart, formData);

    if (res == "success") {
      getCartDetails();
    }
  }

  async function getCartDetails() {
    let data = await fetchGet(urls.getCartDetails);
    if (data.count && data.count > 0) {
      let counterEl = document.querySelector("#cart-counter");
      let cartBodyEl = document.querySelector("#cart-offcanvas-body");

      let cartCount = data.count;
      let html = ``;
      let total = 0;
      counterEl.innerHTML = cartCount;

      data.items.forEach((item) => {
        let itemTotal = item.product__price * item.quantity;
        html += ` <div class="d-flex justify-content-around cart-item">
           <div class="d-flex">
              <img class="offcanvas-cart-image" src="${staticPath}${item.product__image}" alt="${item.product__name}" />
              <div class="mx-2">${item.product__name}</div>
           </div>
           <button id="cartRemove-${item.id}" class="btn btn-cart-remove text-main">
            <i title="Remove" class="fas fa-trash"></i>
           </button>
          </div>
          <div class="d-flex justify-content-between align-items-center pt-2 px-4">
            <div>Price: ${item.product__price} ${currency}</div>
            <div>X</div>
            <input id="cartItem-${item.id}-${item.product__price}" type="number" class="form-control text-center cart-textbox" min="1" value="${item.quantity}"/>
            <div> = </div>
            <div> <span id="cartItemTotal-${item.id}"> ${itemTotal.toFixed(2)}</span> ${currency}</div>
          </div>
          <hr>
        `;
        total += item.quantity * item.product__price;
      });

      html = `
      <div>
        ${html}
        <div class="d-flex justify-content-end px-4 fs-4">
         <div class="">Total</div>
         <div class="mx-3"> = </div>
         <div> <span id="cartTotal">${total.toFixed(2)}</span> ${currency}</div>
        </div>
        <div class="text-center mt-1">
          <a href="${urls.checkout}" class="w-50 btn bg-main text-white">Checkout</a>
        </div>
        <hr>
      </div>
      `;

      cartBodyEl.innerHTML = html;

      inEls = document.querySelectorAll(".cart-textbox");
      btnEls = document.querySelectorAll(".btn-cart-remove");

      inEls.forEach((el) => {
        el.addEventListener("change", (e) => {
          updateCart(e);
        });
      });

      btnEls.forEach((el) => {
        el.addEventListener("click", (e) => {
          removeCart(e);
        });
      });
    } else {
      let counterEl = document.querySelector("#cart-counter");

      counterEl.innerHTML = 0;
    }
  }
};
