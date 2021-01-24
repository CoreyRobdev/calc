let grid = [];

for (let i=1; i <= 16;i++) {
  grid.push(document.getElementById(i.toString));
}
grid[5] = "snakeHead";

function up() {
  for (let i=0; i < grid.length; i++){
    if (grid[i] === "snakeHead"){
      if (i-4 <= 0) {
        grid.splice(i, 1, null);
        grid[i+12] = "snakeHead";
      }else{
        grid.splice(i, 1, '');
        grid[i-4] = "snakeHead";
      }
    }
  }
  console.log(grid);
}
function left() {
  for (let i=0; i < grid.length; i++){
    if (grid[i] === "snakeHead"){
      if (i === 0 || i === 4 || i === 8 || i === 12) {
        grid.splice(i, 1, null);
        grid[i+3] = "snakeHead";
      }else{
        grid.splice(i, 1, '');
        grid[i-1] = "snakeHead";
      }
    }
  }
  console.log(grid);
}
function right() {
  for (let i=0; i < grid.length; i++){
    if (grid[i] === "snakeHead"){
      if (i === 3 || i === 7 || i === 11 || i === 15) {
        grid.splice(i, 1, null);
        grid[i-3] = "snakeHead";
      }else{
        grid.splice(i, 1, '');
        grid[i+1] = "snakeHead";
      }
    }
  }
  console.log(grid);
}
function down() {
  for (let i=0; i < grid.length; i++){
    if (grid[i] === "snakeHead"){
      if (i === 12 || i === 13 || i === 14 || i === 15) {
        grid.splice(i, 1, null);
        grid[i-12] = "snakeHead";
      }else{
        grid.splice(i, 1, '');
        grid[i+4] = "snakeHead";
      }
    }
  }
  console.log(grid);
}


console.log(grid);