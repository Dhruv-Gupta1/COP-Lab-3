// Add new post to the list of recent posts
function addPost(title, text, author) {
    var posts = document.getElementById("posts");
    var post = document.createElement("li");
post.innerHTML = "<h3>" + title + "</h3>" + "<p>" + text + "</p>" + "<div class='author'>" + author + "</div>";
posts.appendChild(post);
}

// Get the form element and add an event listener to handle form submission
var form = document.getElementById("post-form");
form.addEventListener("submit", function(event) {
event.preventDefault();
var title = document.getElementById("title").value;
var text = document.getElementById("text").value;
var author = document.getElementById("author").value;
addPost(title, text, author);
form.reset();
});
  