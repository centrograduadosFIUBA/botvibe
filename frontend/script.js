document.addEventListener('DOMContentLoaded', () => {
    const userInput = document.getElementById('user-input');
    const sendButton = document.getElementById('send-button');
    const chatMessages = document.getElementById('chat-messages');
    const typingIndicator = document.getElementById('typing-indicator');

    const sendMessage = async () => {
        const message = userInput.value.trim();
        if (message === '') return;

        addMessageToChat(message, 'user');
        userInput.value = '';
        typingIndicator.style.visibility = 'visible'; // Mostrar animación

        try {
            const response = await fetch('http://127.0.0.1:8000/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ message: message })
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();
            addMessageToChat(data.response, 'gpt', true); // Pasar true para indicar que es HTML
        } catch (error) {
            console.error('Error al enviar mensaje:', error);
            addMessageToChat('Lo siento, hubo un error al comunicarse con el bot.', 'gpt');
        } finally {
            typingIndicator.style.visibility = 'hidden'; // Ocultar animación
        }
    };

    sendButton.addEventListener('click', sendMessage);

    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });

    function addMessageToChat(content, sender, isHtml = false) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message', sender);

        const bubbleDiv = document.createElement('div');
        bubbleDiv.classList.add('message-bubble');
        
        if (isHtml) {
            bubbleDiv.innerHTML = content; // Insertar como HTML
        } else {
            bubbleDiv.textContent = content; // Insertar como texto plano
        }

        messageDiv.appendChild(bubbleDiv);
        chatMessages.appendChild(messageDiv);

        // Desplazar hacia abajo para ver el último mensaje
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
});
