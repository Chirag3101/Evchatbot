from fastapi import FastAPI, Form, Request
from twilio.twiml.messaging_response import MessagingResponse

app = FastAPI()

EV_STATIONS = {
    "Delhi": ["Station A - Connaught Place", "Station B - Saket"],
    "Mumbai": ["Station C - Bandra", "Station D - Navi Mumbai"],
}

JOURNEY_CHECKLIST = {
    "car": ["Fuel/Electric Charge", "Driver’s License", "Tire Pressure Check", "Emergency Kit"],
    "bike": ["Helmet", "Fuel", "Riding Gear", "Tool Kit"],
    "bus": ["Ticket/Pass", "Water Bottle", "Headphones", "Hand Sanitizer"]
}

@app.post("/webhook")
async def whatsapp_webhook(Body: str = Form(...)):
    print(f"Received message: {Body}")
    return {"status": "received", "message": Body}

@app.post("/whatsapp")
async def whatsapp_reply(request: Request):
    form = await request.form()
    user_message = form.get("Body").strip().title()
    resp = MessagingResponse()

    if user_message in EV_STATIONS:
        stations = "\n".join(EV_STATIONS[user_message])
        resp.message(f"🔋 EV Charging Stations in {user_message}:\n{stations}")

    elif user_message.lower().startswith("plan trip to"):
        parts = user_message.split()
        if len(parts) >= 5:  # Expected format: "Plan trip to <destination> by <mode>"
            mode = parts[-1].lower()
            checklist = JOURNEY_CHECKLIST.get(mode, ["Basic Travel Essentials"])
            resp.message(f"🧳 Checklist for {mode} travel:\n" + "\n".join(checklist))
        else:
            resp.message("Usage: 'Plan trip to <destination> by <car/bike/bus>'")

    else:
        resp.message("Send a city name for EV stations or 'Plan trip to <destination> by <car/bike/bus>'.")

    return str(resp)
