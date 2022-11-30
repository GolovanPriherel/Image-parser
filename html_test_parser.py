import requests

from openvpn_api import VPN
v = VPN('127.0.0.1', 7505)

with v.connection():
    response = requests.get("https://rule34.com")
    print(response)
    print(v.release)
