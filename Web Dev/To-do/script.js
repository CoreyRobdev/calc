//these dont have to be global but aye
let main = document.getElementById("main");
let title;
let postCount=2;

function post(){
  postCount++;
  title = document.getElementById("title").value;
  let paragraph = document.getElementById("paragraph").value;

  let post = document.createElement('div');
  let postTitle = document.createElement("h1");
  let postContent = document.createElement("p");

  post.className = "post";
  postTitle.innerHTML = title;
  postContent.innerHTML = paragraph;
  main.appendChild(post);
  post.appendChild(postTitle);
  post.appendChild(postContent);
  post.id = "post" + postCount;

//navigation
  let listItem = document.createElement("li");
  let link = document.createElement("a");
  link.innerHTML = title;

  let list = document.getElementById("list");
  listItem.appendChild(link);
  list.appendChild(listItem);
  link.href = "#" + post.id;
}
