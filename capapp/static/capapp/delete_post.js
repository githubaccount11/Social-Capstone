

function delete_post(post) {
    var userSelection = confirm("Are you sure you want to delete this post?");
    
    if (userSelection == true){
        fetch(`/delete_post/${post}`)
        .then( () => {
            alert("Your post was deleted!")
            window.location('/')
        })
    } else {
        alert("Your post is not deleted!");
    }
}