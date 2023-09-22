const axios = require("axios");
const fs = require("fs");

const image = fs.readFileSync("/home/mathi/Downloads/undefined.jpeg", {
    encoding: "base64"
});

axios({
    method: "POST",
    url: "https://detect.roboflow.com/cell_finds/3",
    params: {
        api_key: "fo2IMw6ZRxQK8Nju9ULP"
    },
    data: image,
    headers: {
        "Content-Type": "application/x-www-form-urlencoded"
    }
})
.then(function(response) {
    console.log(response.data);
})
.catch(function(error) {
    console.log(error.message);
});