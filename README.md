# WhatsApp Messaging API

This project is a Flask-based API that allows sending text messages and PDF documents via WhatsApp using the Meta (Facebook) WhatsApp Cloud API.

## Features
- Send text messages to WhatsApp users.
- Send PDF documents to WhatsApp users.
- Securely store API credentials using environment variables.

## Prerequisites
1. Python 3.x installed on your system.
2. A Meta (Facebook) Developer account with access to the WhatsApp Cloud API.
3. A registered WhatsApp Business phone number.
4. An `ACCESS_TOKEN` and `PHONE_NUMBER_ID` from the WhatsApp Cloud API.
5. A `.env` file to store sensitive credentials.

## Installation
### 1. Clone the Repository
```sh
git clone https://github.com/HimanshuChelani27/whatsappIntegration.git
cd whatsappIntegration
```

### 2. Create a Virtual Environment (Optional but Recommended)
```sh
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file in the root directory and add the following:
```ini
WHATSAPP_ACCESS_TOKEN=your_facebook_whatsapp_access_token
WHATSAPP_PHONE_NUMBER_ID=your_whatsapp_phone_number_id
```

## Usage
### Run the Flask Server
```sh
python app.py
```

### API Endpoints

#### 1. Send a Text Message
**Endpoint:** `POST /send_text`

**Request Body:**
```json
{
  "phone": "1234567890",
  "message": "Hello from WhatsApp API!"
}
```

**Response:**
```json
{
  "messaging_product": "whatsapp",
  "contacts": [{ "input": "919876543210", "wa_id": "919876543210" }],
  "messages": [{ "id": "wamid..." }]
}
```

#### 2. Send a PDF Document
**Endpoint:** `POST /send_pdf`

**Request Body:**
```json
{
  "phone": "9876543210",
  "file_url": "https://example.com/sample.pdf"
}
```

**Response:**
```json
{
  "messaging_product": "whatsapp",
  "contacts": [{ "input": "919876543210", "wa_id": "919876543210" }],
  "messages": [{ "id": "wamid..." }]
}
```

## Error Handling
- Invalid phone number returns `{ "error": "Invalid phone number", "status": 400 }`
- API request failures return `{ "error": "RequestException message", "status": 500 }`


## Author
Your Name - [HimanshuChelani27](https://github.com/HimanshuChelani27)

