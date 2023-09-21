document.addEventListener('DOMContentLoaded', () => {
    const userInput = document.getElementById('user-input');
    const sendButton = document.getElementById('send-button');
    const chatResponses = document.querySelector('.chat-responses');

    sendButton.addEventListener('click', () => {
        const userMessage = userInput.value.trim();
        if (userMessage !== '') {
            // Display user message in chat history
            appendMessage('You', userMessage, 'right');

            // Show loading indicator while waiting for a response
            appendLoadingIndicator();

            // Send the user input to the server using a fetch request
            fetch('/get_response', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ user_input: userMessage }),
            })
            .then(response => response.json())
            .then(data => {
                // Remove loading indicator
                removeLoadingIndicator();

                // Display the response from the server in the chat
                appendResponse('Bot', data.response);
            })
            .catch(error => {
                console.error('Error:', error);
                removeLoadingIndicator();
            });

            userInput.value = '';
        }
    });

    function appendMessage(sender, message, alignment) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${alignment}`;
        messageDiv.innerHTML = `${sender}: ${message}`;
        chatResponses.appendChild(messageDiv);
        chatResponses.scrollTop = chatResponses.scrollHeight;
    }

    function appendLoadingIndicator() {
        const loadingDiv = document.createElement('div');
        loadingDiv.className = 'loading-indicator';
        loadingDiv.innerHTML = '<span>Loading...</span>';
        chatResponses.appendChild(loadingDiv);
        chatResponses.scrollTop = chatResponses.scrollHeight;
    }

    function removeLoadingIndicator() {
        const loadingIndicator = chatResponses.querySelector('.loading-indicator');
        if (loadingIndicator) {
            loadingIndicator.remove();
        }
    }

    function appendResponse(sender, response) {
        const responseDiv = document.createElement('div');
        responseDiv.className = 'message';
        responseDiv.innerHTML = `${sender}: ${response}`;
        chatResponses.appendChild(responseDiv);
        chatResponses.scrollTop = chatResponses.scrollHeight;
    }
});
