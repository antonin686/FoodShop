async function fetchGet(url) {
  let response = await fetch(url);
  let res = await response.json();
  return res;
}

async function fetchPost(url, data) {
  let response = await fetch(url, {
    method: "POST",
    body: data,
    headers: { 
        'X-CSRFToken': csrf
    },
  });

  let res = await response.text();
  return res;
}
