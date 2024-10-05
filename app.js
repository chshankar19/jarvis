document.getElementById('send-btn').addEventListener('click', function () {
    const userInput = document.getElementById('user-input').value;
    if (userInput) {
        displayUserMessage(userInput);
        getChatbotResponse(userInput);
        document.getElementById('user-input').value = '';
    }
});

function displayUserMessage(message) {
    const chatOutput = document.getElementById('chat-output');
    const userMessage = document.createElement('div');
    userMessage.classList.add('message', 'user-message', 'clearfix');
    userMessage.innerText = message;
    chatOutput.appendChild(userMessage);
    chatOutput.scrollTop = chatOutput.scrollHeight;
}

function displayBotMessage(message) {
    const chatOutput = document.getElementById('chat-output');
    const botMessage = document.createElement('div');
    botMessage.classList.add('message', 'bot-message', 'clearfix');
    botMessage.innerText = message;
    chatOutput.appendChild(botMessage);
    chatOutput.scrollTop = chatOutput.scrollHeight;
}

async function getChatbotResponse(userInput) {
    const response = await fetch('http://127.0.0.1:5000/chat', {
        method: 'POST',  // Ensure it's POST, not GET
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ prompt: userInput })
    });
    const data = await response.json();
    displayBotMessage(data.response);
}


