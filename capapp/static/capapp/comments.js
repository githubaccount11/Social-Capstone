function showComments(comment, parent_id, user_id, post_id) {
    // do something with comment
    const collapseDiv = document.createElement("div")
    collapseDiv.setAttribute("name", `collapse-${parent_id}`)
    const div = document.createElement("div")
    const figure = document.createElement("figure")
    figure.className = "bg-slate-50 rounded-xl p-8 m-2"
    const figureDiv = document.createElement("div")
    figureDiv.className = "space-y-4"
    div.setAttribute("id",`comment-${comment.comment.id}`);
    let parent;
    if (parent_id == 0) {
        parent = document.querySelector("#comments")
    } else {
        parent = document.querySelector(`#comment-${parent_id}`)
    }
    div.classList.add(`pl-5`)
    figure.appendChild(figureDiv)
    div.appendChild(figure)
    collapseDiv.appendChild(div)
    parent.appendChild(collapseDiv)
    
    const a = document.createElement("a")
    a.href = `../profile/${comment.comment.user__id}`
    a.className = "text-slate-500 pr-3"
    figureDiv.appendChild(a)

    const firstSpan = document.createElement("span")
    firstSpan.textContent = comment.comment.user__first_name + " "
    a.appendChild(firstSpan)
    const lastSpan = document.createElement("span")
    lastSpan.textContent = comment.comment.user__last_name + " "
    a.appendChild(lastSpan)

    const createdSpan = document.createElement("span")
    createdSpan.className = "text-slate-500 px-3"
    let dateTime = moment(comment.comment.date_created);
    dateTime = moment(dateTime).format('MMMM Do YYYY, h:mm a');
    createdSpan.textContent = `Created: ${dateTime}`
    figureDiv.appendChild(createdSpan)

    const editedSpan = document.createElement("span")
    editedSpan.className = "text-slate-500 px-3"
    let editedDateTime = moment(comment.comment.date_edited);
    editedDateTime = moment(editedDateTime).format('MMMM Do YYYY, h:mm a');
    editedSpan.textContent = `Edited: ${editedDateTime}`
    figureDiv.appendChild(editedSpan)

    const pre = document.createElement("pre")
    pre.className = "font-sans"
    pre.textContent = comment.comment.text_content
    figureDiv.appendChild(pre)

    const collapse = document.createElement("button")
    collapse.addEventListener("click", function(event) {
        toCollapse = document.getElementsByName(`collapse-${comment.comment.id}`)
        // console.log(toCollapse)
        for (collapsable of toCollapse) {
            // console.log(collapsable)
            if (collapsable.style.display == "block") {
                collapsable.style.display = "none"
            } else {
                collapsable.style.display = "block"
            }
        }
    })
    collapse.textContent = "...";
    
    figureDiv.appendChild(collapse)

    const makeComment = document.createElement("a")
    makeComment.textContent = "Comment"
    makeComment.className = "mx-4 inline-block px-6 py-2.5 bg-sky-200 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-sky-300 hover:shadow-lg focus:bg-sky-300 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-sky-400 active:shadow-lg transition duration-150 ease-in-out"
    makeComment.href = `../make_comment/${post_id}/${comment.comment.id}`
    figureDiv.appendChild(makeComment)
    
    if (user_id == comment.comment.user__id) {
        const editComment = document.createElement("a")
        editComment.textContent = "Edit"
        editComment.className = "inline-block px-6 py-2.5 bg-rose-200 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-rose-300 hover:shadow-lg focus:bg-rose-300 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-rose-400 active:shadow-lg transition duration-150 ease-in-out"
        editComment.href = `../edit_comment/${comment.comment.id}`
        figureDiv.appendChild(editComment)
        const deleteComment = document.createElement("a")
        deleteComment.textContent = "Delete"
        deleteComment.className = "cursor-pointer mx-4 inline-block px-6 py-2.5 bg-yellow-200 text-white font-medium text-xs leading-tight uppercase rounded shadow-md hover:bg-yellow-300 hover:shadow-lg focus:bg-yellow-300 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-yellow-400 active:shadow-lg transition duration-150 ease-in-out"
        deleteComment.addEventListener("click", () => delete_comment(comment.comment.id))
        figureDiv.appendChild(deleteComment)
    }

    for (subment of comment.subments) {
        showComments(subment, comment.comment.id, user_id, post_id)
    }
}

fetch(`/get_comments/${post}`)
.then(response => response.json())
.then(data => {
    for (comment of data.data[0]) {
        showComments(comment, 0, data.data[1], data.data[2])
    }
})