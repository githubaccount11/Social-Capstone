
function showComments(comment, parent_id, depth) {
    // do something with comment
    collapseDiv = document.createElement("div")
    collapseDiv.id = `collapse-${parent_id}`
    collapseDiv.className = "collapse"
    div = document.createElement("div")
    div.setAttribute("id",`comment-${comment.comment.id}`);
    let parent;
    if (depth == 0) {
        parent = document.querySelector("#comments")
    } else {
        parent = document.querySelector(`#comment-${parent_id}`)
    }
    div.classList.add(`pl-${(depth * 5)}`)
    collapseDiv.appendChild(div)
    parent.appendChild(collapseDiv)
    
    const a = document.createElement("a")
    a.href = `../profile/${comment.comment.user__id}`
    div.appendChild(a)

    const firstSpan = document.createElement("span")
    firstSpan.textContent = comment.comment.user__first_name + " "
    a.appendChild(firstSpan)
    const lastSpan = document.createElement("span")
    lastSpan.textContent = comment.comment.user__last_name + " "
    a.appendChild(lastSpan)

    const createdSpan = document.createElement("span")
    createdSpan.textContent = `created: ${comment.comment.date_created} `
    div.appendChild(createdSpan)

    const editedSpan = document.createElement("span")
    editedSpan.textContent = `edited: ${comment.comment.date_edited}`
    div.appendChild(editedSpan)

    const p = document.createElement("p")
    p.textContent = comment.comment.text_content
    div.appendChild(p)

    const collapse = document.createElement("a")
    collapse.textContent = "...";
    collapse.className = "inline-block px-6 py-2.5 bg-blue-600 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-blue-700 hover:shadow-lg focus:bg-blue-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-blue-800 active:shadow-lg transition duration-150 ease-in-out";
    collapse.setAttribute("data-bs-toggle", "collapse");
    collapse.href = `#collapse-${comment.comment.id}` ;
    collapse.role = "button";
    collapse.setAttribute("aria-expanded", "true");
    collapse.setAttribute("aria-controls", `collapse-${comment.comment.id}`);
    div.appendChild(collapse)

    const makeComment = document.createElement("a")
    makeComment.textContent = "Comment"
    makeComment.href = `../make_comment/${comment.comment.post_id}/${comment.comment.id}`
    div.appendChild(makeComment)
    
    if (user_id == comment.comment.user__id) {
        const editComment = document.createElement("a")
        editComment.textContent = "Edit"
        editComment.href = `../edit_comment/${comment.comment.id}`
        div.appendChild(editComment)
    }

    for (subment of comment.subments) {
        showComments(subment, comment.comment.id, depth + 1)
    }
}

fetch(`/get_comments/${post}`)
.then(response => response.json())
.then(data => {
    results = data.data
    console.log(results)
    for (comment of results) {
        showComments(comment, 0, 0)
    }
})