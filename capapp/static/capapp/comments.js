const comments = document.querySelector("#comments")

function showComments(comment) {
    // do something with comment

    
    for (subment of comment.subment) {
        showComments(subment)
    }
}

fetch(`/get_comments/${post.id}`)
.then(response => response.json())
.then(data => {
    results = data.data
    for (comment of results) {
        showComments(comment)
    }
})