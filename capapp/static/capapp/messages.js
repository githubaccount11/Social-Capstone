const sendBtn = document.getElementById('send-btn')
const messageBox = document.getElementById('message-box')
const parent = document.querySelector("#messages")

sendBtn.addEventListener("click", function() {
    console.log(messageBox.value)
    fetch(`/send_message/${friend}/${messageBox.value}`)
    .then(response => response.json())
    .then(data => {
        messageBox.textContent = ""
        fetchMessages()
})
})

function showMessages(message) {
    // do something with comment
    const figure = document.createElement("figure")
    figure.className = "bg-slate-50 rounded-xl p-8 m-2"
    const figureDiv = document.createElement("div")
    figureDiv.className = "space-y-4"
    figure.appendChild(figureDiv)
    parent.appendChild(figure)

    const createdSpan = document.createElement("span")
    createdSpan.className = "text-slate-500 px-3"
    let dateTime = moment(message.message.date_created);
    dateTime = moment(dateTime).format('MMMM Do YYYY, h:mm a');
    createdSpan.textContent = `Created: ${dateTime}`
    figureDiv.appendChild(createdSpan)

    const p = document.createElement("p")
    p.textContent = message.message.text_content
    figureDiv.appendChild(p)
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