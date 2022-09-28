const sendBtn = document.getElementById('send-btn')
const messageBox = document.getElementById('message-box')
const parent = document.querySelector("#messages")

sendBtn.addEventListener("click", function() {
    fetch(`/send_message/${friend}/${messageBox.value}`)
    .then( () => {
        messageBox.value = ""
        fetchMessages()
    })
})

function showMessages(message) {
    // do something with comment
    const div = document.createElement("div")
    const figure = document.createElement("figure")
    figure.className = "bg-slate-50 rounded-xl p-8 m-2"
    const figureDiv = document.createElement("div")
    figureDiv.className = "space-y-4"
    const flexDiv = document.createElement("div")
    flexDiv.className = "flex"
    figureDiv.appendChild(flexDiv)
    figure.appendChild(figureDiv)
    div.appendChild(figure)
    parent.appendChild(div)
    const dateAndImageDiv = document.createElement("div")

    const createdSpan = document.createElement("span")
    createdSpan.className = "text-slate-500 px-3"
    let dateTime = moment(message.message.date_created);
    dateTime = moment(dateTime).format('MMMM Do YYYY, h:mm a');
    createdSpan.textContent = `Created: ${dateTime}`

    const imageA = document.createElement("a")
    imageA.href = `../profile/${message.message.user_id}`
    const image = document.createElement("img")
    image.className = "border w-24 h-24 rounded-full"
    image.src = message.message.profile_image
    image.alt = `${message.message.first_name} ${message.message.last_name}'s profile picture`
    imageA.appendChild(image)

    const p = document.createElement("p")
    p.textContent = message.message.text_content
    
    if (message.message.user_id == user_self) {
        div.className = "ml-10"
        flexDiv.classList.add("text-right", "justify-end")
        
        flexDiv.appendChild(p)
        dateAndImageDiv.appendChild(createdSpan)
        const imageDiv = document.createElement("div")
        imageDiv.className = "flex justify-end"
        dateAndImageDiv.appendChild(imageDiv)
        imageDiv.appendChild(imageA)
        flexDiv.appendChild(dateAndImageDiv)

    } else {
        div.className = "mr-10"
        
        flexDiv.appendChild(dateAndImageDiv)
        dateAndImageDiv.appendChild(createdSpan)
        dateAndImageDiv.appendChild(imageA)
        flexDiv.appendChild(p)
    }                     

}

fetchMessages()

function fetchMessages() {
    fetch(`/get_messages/${friend}`)
    .then(response => response.json())
    .then(data => {
        console.log(data.data)
        parent.innerHTML = ""
        for (message of data.data.messages) {
            showMessages(message)
        }
        window.scrollTo(0,document.body.scrollHeight);
    })
}