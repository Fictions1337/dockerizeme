const url = "http://91.99.128.94:8000/message";
fetch(url)
    .then(response => response.json())
    .then(data => {
        document.getElementById("message").innerText = data.message;
    })
    .catch(error => {
        document.getElementById("message").innerText = "Error";
        console.error(error);
    });