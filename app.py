from flask import Flask, request
import requests

app = Flask(__name__)

# Helper to get country from ip

def get_country(ip):
    try:
        # Query ipapi.co for geolocation info
        resp = requests.get(f"https://ipapi.co/{ip}/json/", timeout=5)
        if resp.ok:
            data = resp.json()
            return data.get("country_name", "Unknown")
    except requests.RequestException:
        pass
    return "Unknown"

@app.route('/')
def index():
    ip = request.remote_addr or 'Unknown'
    country = get_country(ip)
    return f"Zdravo, moja IP adresa je {ip} i nalazis se u drzavi {country}."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
