const messageInput = document.getElementById('messageInput');
const detectBtn = document.getElementById('detectBtn');
const resultContent = document.getElementById('resultContent');

function fillExample(text) {
    messageInput.value = text;
}

async function detectSpam() {
    const message = messageInput.value.trim();
    if (!message) return;

    detectBtn.disabled = true;
    detectBtn.innerText = "PROCESSING...";

    try {
        const response = await fetch('http://127.0.0.1:8000/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: message }),
        });

        const data = await response.json();
        const isSpam = data.is_spam;
        
        resultContent.innerHTML = `
            <div class="res-box ${isSpam ? 'spam' : 'ham'}">
                <h2 style="margin-bottom: 8px;">${isSpam ? '⚠️ SPAM DETECTED' : '✅ MESSAGE SECURE'}</h2>
                <p style="color: white; opacity: 0.9;">"${data.message}"</p>
                <p style="margin-top: 10px; font-size: 0.8rem; font-weight: bold;">RESULT: ${data.prediction.toUpperCase()}</p>
            </div>
        `;

    } catch (error) {
        resultContent.innerHTML = `<p style="color: #ff4d4d;">Error connecting to API. Ensure backend is running.</p>`;
    } finally {
        detectBtn.disabled = false;
        detectBtn.innerText = "🚀 DETECT SPAM";
    }
}

detectBtn.addEventListener('click', detectSpam);