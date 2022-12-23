var td = document.querySelectorAll("td")
var restart = document.querySelector(".btn") 

td.forEach(
  function(item) {
    item.addEventListener('click', function () {
    if (item.textContent === "") {
      item.textContent = 'X';
    } else if (item.textContent === "X") {
      item.textContent = 'O';
    } else if (item.textContent === "O") {
      item.textContent = '';
    }
  })})

restart.addEventListener('click', function () {td.forEach(function(x) {x.textContent = ""})})