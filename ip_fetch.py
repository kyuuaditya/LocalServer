import socket
import psutil
import requests
import credentials

# use this to extract ip address if your batch script is unable to identify psutil OR you dont want to install psutil.
# NOTE: this might not work if you also have ethernet connection setup due to the presence of 2 IPv4 addresses in the same location.

# hostname = socket.gethostname()
# local_ip = socket.gethostbyname(hostname)

# this always returns the wifi IPv4 address and does not return the ethernet address.
def get_ipv4_address():
    for interface, addrs in psutil.net_if_addrs().items():
        for addr in addrs:
            if addr.family == socket.AF_INET and "Wi-Fi" in interface:  # Adjust for your system
                return addr.address
    return "No Wi-Fi IPv4 found"

local_ip = get_ipv4_address()

# edit this message as per your preferences.
message = f"Local Server link: {local_ip}:8008"
url = f"https://api.telegram.org/bot{credentials.BOT_TOKEN}/sendMessage?chat_id={credentials.CHAT_ID}&text={message}"
requests.get(url)
print("Sent IP to Telegram!")
