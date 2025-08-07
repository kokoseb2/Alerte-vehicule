from flask import Flask
import requests
import time

app = Flask(__name__)

last_notification_time = 0
NOTIFICATION_DELAY = 5 * 60  # 5 minutes

@app.route("/")
def send_notification():
    global last_notification_time
    current_time = time.time()

    if current_time - last_notification_time >= NOTIFICATION_DELAY:
        requests.post("https://api.pushover.net/1/messages.json", data={
            "token": "aqyp8jk1dpc3qvxuz61psqtkarus1r",
            "user": "ukn2g8tkemb9q6124egezsysfkyyc6",
            "message": "🚗 Une personne signale que votre véhicule dérange.",
            "title": "📣 Alerte QR Code",
            "priority": 1
        })
        last_notification_time = current_time
        return """
            ✅ <strong>Alerte transmise au propriétaire.</strong><br><br>
            Merci pour votre signalement.
        """
    else:
        return """
            ⏳ <strong>Le propriétaire a déjà été prévenu récemment.</strong><br><br>
            Merci de patienter quelques minutes.
        """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
