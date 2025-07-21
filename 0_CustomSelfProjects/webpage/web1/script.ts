const messagesDiv = document.getElementById('messages') as HTMLDivElement;
const userInput = document.getElementById('userInput') as HTMLInputElement;
const sendBtn = document.getElementById('sendBtn') as HTMLButtonElement;

function addMessage(who: string, text: string) {
  const msg = document.createElement('div');
  msg.textContent = who + ": " + text;
  messagesDiv.appendChild(msg);
  messagesDiv.scrollTop = messagesDiv.scrollHeight;
}

sendBtn.onclick = () => {
  const userText = userInput.value;
  if (userText.trim() === "") return;
  addMessage("You", userText);
  userInput.value = "";
  // Fake AI response for demo
  setTimeout(() => addMessage("AI", "You said: " + userText), 700);
};
