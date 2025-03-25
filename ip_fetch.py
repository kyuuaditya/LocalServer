import socket
import requests
import credentials

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

message = f"🔹 Your Local Server link: {local_ip}:8008"
url = f"https://api.telegram.org/bot{credentials.BOT_TOKEN}/sendMessage?chat_id={credentials.CHAT_ID}&text={message}"
requests.get(url)
print("Sent IP to Telegram!")
