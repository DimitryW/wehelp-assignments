
let i = 0;
function getData(callback) {
    let list_name = [];
    let list_img = [];
    let req = new XMLHttpRequest();
    req.open("get", "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json");
    req.onload = function () {
        let result = JSON.parse(this.responseText).result.results;
        for (let i in result) {
            list_name.push(result[i]["stitle"]);
        }
        for (let i in result) {
            list_img.push("https" + result[i]["file"].split("https")[1]);
        }
        console.log(list_name.length);
        callback(list_name, list_img);
    }
    req.send();
}

let len = 0
function showData(list_name, list_img) {
    for (let count = 1; count <= 8; count++) {
        if (len < list_name.length) {
            let img = document.createElement("img");
            let div1 = document.createElement("div");
            let div2 = document.createElement("div");
            let div3 = document.createElement("div");
            let div4 = document.createElement("div");
            let text = document.createTextNode(list_name[i]);
            img.src = list_img[i];
            div1.id = "box" + i;
            div2.id = "p" + i;
            div3.id = "div" + i;
            div4.className = "title";
            div4.appendChild(text);
            document.getElementById("main").appendChild(div1);
            document.getElementById("box" + i).appendChild(div2);
            document.getElementById("box" + i).appendChild(div3);
            document.getElementById("p" + i).appendChild(img);
            document.getElementById("div" + i).appendChild(div4);
            console.log("i=" + i);
            console.log("count=" + count);
            i++;
            len++;
        }
        console.log("len="+len);
    }
}

