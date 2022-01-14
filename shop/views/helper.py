
from pprint import pprint
from ..models import Review, Order

def checkIfCanReview(customer, product):
    order = Order.objects.filter(customer_id=customer).first()
    if order is not None:
        productOrderCount = order.items.filter(
            product_id=product).count()
        if productOrderCount > 0:
            review = Review.objects.filter(customer_id=customer, product_id=product).first()
            if review is None:
                return True
    return False