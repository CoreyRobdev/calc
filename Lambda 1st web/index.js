var button = document.getElementById("top");

button.onmouseover = function() {
  this.style.backgroundColor = "white";
};
button.onmouseout = function() {
  this.style.backgroundColor = "olivedrab";
};

function topFunc() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}
