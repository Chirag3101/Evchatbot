# Saathi.EV - EV Charging Insights Chatbot

## Overview
An AI-driven WhatsApp chatbot that helps EV users find nearby charging stations, check availability, and plan optimal routes.

## Features
- 📍 **Find Nearby EV Chargers** - Get a list of charging stations in your city.
- ⚡ **Check Availability** - View real-time charger availability and wait times.
- 🗺 **Route Planning** - Get optimized charging stops for long trips.
- 🔌 **Charger Type Info** - Know whether a station has fast or slow chargers.
- 🔹 **Integration with real-time charging station databases** - Access the latest charging station updates.
- 🔹 **AI-driven personalized journey recommendations** - Get tailored route suggestions based on your travel needs.
- 🔹 **Multi-language support** - Communicate in your preferred language.

## Tech Stack
- **Backend:** FastAPI
- **Messaging:** Twilio WhatsApp API
- **EV Data:** Google Maps API (Places, Directions, Distance Matrix)
- **Hosting:** Ngrok (for local development)

## Setup Guide
### 1️⃣ Install Dependencies
```bash
pip install fastapi uvicorn twilio python-dotenv
```

### 2️⃣ Set Up Environment Variables
Create a `.env` file with:
```
TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE_NUMBER=your_twilio_whatsapp_number
GOOGLE_MAPS_API_KEY=your_google_maps_api_key
```

### 3️⃣ Run the Server
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

### 4️⃣ Expose Locally Using Ngrok
```bash
ngrok http 8000
```
Use the generated `https://your-ngrok-url/webhook` in Twilio settings.

### 5️⃣ Deploy & Test
- Connect Twilio webhook to `/webhook`
- Send "Find EV Charger" in WhatsApp to test responses.

## API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/webhook` | Receives messages from WhatsApp |
| POST | `/whatsapp` | Processes user queries and sends responses |

## Sample Chatbot Interactions
### 🔍 Finding EV Chargers
**User:** Find EV Charger near me  
**Saath.EV:** Please share your city name (e.g., "Delhi")

**User:** Delhi  
**Saath.EV:** 🔋 EV Charging Stations in Delhi:  
- Station A - Connaught Place  
- Station B - Saket  

**User:** Mumbai  
**Saath.EV:** 🔋 EV Charging Stations in Mumbai:  
- Station C - Bandra  
- Station D - Navi Mumbai  

### ⏳ Checking Charger Availability
**User:** Is there an available charger in Bandra?
**Saath.EV:** Checking real-time data... ✅ Fast Charger available at Station C - Bandra.

### 🛣 Route Planning
**User:** Plan my route from Delhi to Agra
**Saath.EV:** 🔋 Recommended charging stops:
1️⃣ Station A - Connaught Place (Fast Charger)  
2️⃣ Station X - Mathura (Superfast Charger)  

### 🌍 Multi-language Support
**User:** चार्जिंग स्टेशन कहाँ है? (Where is the charging station?)
**Saath.EV:** कृपया अपना शहर का नाम भेजें (e.g., "दिल्ली").

🚀 **Contribute & Star this Repo!**

