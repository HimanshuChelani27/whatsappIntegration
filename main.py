import os
import json
import requests
from flask import Flask, request, jsonify
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# WhatsApp API credentials (store these in .env for security)
ACCESS_TOKEN = os.getenv("WHATSAPP_ACCESS_TOKEN")
PHONE_NUMBER_ID = os.getenv("WHATSAPP_PHONE_NUMBER_ID")
VERSION = "v20.0"

# Base URL for WhatsApp API
BASE_URL = f"https://graph.facebook.com/{VERSION}/{PHONE_NUMBER_ID}/messages"

# Headers for WhatsApp API requests
HEADERS = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

# WhatsApp Messaging Class
class WhatsApp:
    @staticmethod
    def send_text_message(phone_number, message):
        """Send a text message via WhatsApp."""
        if not phone_number or len(phone_number) != 10:
            return {"error": "Invalid phone number", "status": 400}

        phone_number = "91" + phone_number  # Adding country code

        data = {
            "messaging_product": "whatsapp",
            "to": phone_number,
            "type": "text",
            "text": {"body": message}
        }

        try:
            response = requests.post(BASE_URL, json=data, headers=HEADERS)
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e), "status": 500}

    @staticmethod
    def send_pdf(phone_number, file_url):
        """Send a PDF document via WhatsApp."""
        if not phone_number or len(phone_number) != 10:
            return {"error": "Invalid phone number", "status": 400}

        phone_number = "91" + phone_number

        data = {
            "messaging_product": "whatsapp",
            "to": phone_number,
            "type": "document",
            "document": {"link": file_url, "filename": "WhatsApp_Document.pdf"}
        }

        try:
            response = requests.post(BASE_URL, json=data, headers=HEADERS)
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e), "status": 500}

# Flask Routes
@app.route("/send_text", methods=["POST"])
def send_text():
    """API endpoint to send a text message."""
    data = request.get_json()
    phone = data.get("phone")
    message = data.get("message")

    response = WhatsApp.send_text_message(phone, message)
    return jsonify(response)

@app.route("/send_pdf", methods=["POST"])
def send_pdf():
    """API endpoint to send a PDF file."""
    data = request.get_json()
    phone = data.get("phone")
    file_url = data.get("file_url")

    response = WhatsApp.send_pdf(phone, file_url)
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
