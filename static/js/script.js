async function sendMessage() {

    const input = document.getElementById("message");
    const message = input.value.trim();

    if (message === "") return;

    const chatBox = document.getElementById("chat-box");

    // Show user message
    chatBox.innerHTML += `
        <div class="user-message">
            ${message}
        </div>
    `;

    input.value = "";

    // Typing indicator
    showTypingIndicator();

    // Send to Flask backend
    const response = await fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: message })
    });

    const data = await response.json();

    // Remove typing indicator
    removeTypingIndicator();

    // Show bot reply
    chatBox.innerHTML += `
        <div class="bot-message">
            ${data.reply}
        </div>
    `;

    chatBox.scrollTop = chatBox.scrollHeight;
}


// Enter key support
document.getElementById("message")
.addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
});


// New chat
function newChat() {

    const chatBox = document.getElementById("chat-box");

    chatBox.innerHTML = "";

    chatBox.innerHTML += `
        <div class="bot-message">
            Hello! I am the Ashinaga AI Assistant.
            How can I help you today?
        </div>
    `;
}


// Typing indicator
function showTypingIndicator() {
    const chatBox = document.getElementById("chat-box");

    const typingDiv = document.createElement("div");
    typingDiv.classList.add("bot-message");
    typingDiv.id = "typing-indicator";
    typingDiv.innerText = "Typing...";

    chatBox.appendChild(typingDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}


// Remove typing indicator
function removeTypingIndicator() {
    const typing = document.getElementById("typing-indicator");
    if (typing) {
        typing.remove();
    }
}



// Assistant modal

function openAssistantModal() {

    document.getElementById("assistant-modal").style.display = "block";
}

function closeAssistantModal() {

    document.getElementById("assistant-modal").style.display = "none";
}


// Developer modal

function openDeveloperModal() {

    document.getElementById("developer-modal").style.display = "block";
}

function closeDeveloperModal() {

    document.getElementById("developer-modal").style.display = "none";
}