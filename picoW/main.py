
import network
import time
from firebase_auth import FirebaseAuth

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
if not wlan.isconnected():
    wlan.connect("", "")
    print("Waiting for Wi-Fi connection", end="...")
    while not wlan.isconnected():
        print(".", end="")
        time.sleep(1)
    print()

api_key = ""
auth = FirebaseAuth(api_key)
auth.sign_up("trial@gmail.com", "Abcd0987")
print("Hello, " + auth.user.mail)

