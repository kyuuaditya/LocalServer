import socket
import psutil
import requests
import credentials

# hostname = socket.gethostname()
# local_ip = socket.gethostbyname(hostname)

def get_ipv4_address():
    for interface, addrs in psutil.net_if_addrs().items():
        for addr in addrs:
            if addr.family == socket.AF_INET and "Wi-Fi" in interface:  # Adjust for your system
                return addr.address
    return "No Wi-Fi IPv4 found"

local_ip = get_ipv4_address()

message = f"🔹 Your Local Server link: {local_ip}:8008"
url = f"https://api.telegram.org/bot{credentials.BOT_TOKEN}/sendMessage?chat_id={credentials.CHAT_ID}&text={message}"
requests.get(url)
print("Sent IP to Telegram!")
