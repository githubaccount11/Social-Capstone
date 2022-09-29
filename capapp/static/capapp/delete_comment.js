

function delete_comment(comment) {
    var userSelection = confirm("Are you sure you want to delete this comment?");
    
    if (userSelection == true){
        fetch(`/delete_comment/${comment}`)
        .then( () => {
            alert("Your comment was deleted!")
            window.location = "/"
        })
    } else {
        alert("Your comment is not deleted!");
    }
}