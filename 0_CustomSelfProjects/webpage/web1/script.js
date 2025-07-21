var messagesDiv = document.getElementById('messages');
var userInput = document.getElementById('userInput');
var sendBtn = document.getElementById('sendBtn');
function addMessage(who, text) {
    var msg = document.createElement('div');
    msg.textContent = who + ": " + text;
    messagesDiv.appendChild(msg);
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
}
sendBtn.onclick = function () {
    var userText = userInput.value;
    if (userText.trim() === "")
        return;
    addMessage("You", userText);
    userInput.value = "";
    // Fake AI response for demo
    setTimeout(function () { return addMessage("AI", "You said: " + userText); }, 700);
};
