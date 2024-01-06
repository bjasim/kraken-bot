from keys import api_key, api_sec

import time
import requests
import urllib.parse
import hashlib
import hmac
import base64


# put your api key below
api_key = ""
# put your private key below
api_sec = ""
api_url = "https://api.kraken.com"

def get_kraken_signature(urlpath, data, secret):
    postdata = urllib.parse.urlencode(data)
    encoded = (str(data['nonce']) + postdata).encode()
    message = urlpath.encode() + hashlib.sha256(encoded).digest()
    mac = hmac.new(base64.b64decode(secret), message, hashlib.sha512)
    sigdigest = base64.b64encode(mac.digest())
    return sigdigest.decode()

def kraken_request(url_path, data, api_key, api_sec):
    headers = {"API-Key": api_key, "API-Sign": get_kraken_signature(url_path, data, api_sec)}
    req = requests.post((api_url + url_path), headers=headers, data=data)
    return req.json()

resp = kraken_request("/0/private/TradesHistory", { "nonce": str(int(1000 * time.time())), "trades": True}, api_key, api_sec)

if resp["error"] == []:
    result = resp["result"]
    trades = result["trades"]
    count = int(result["count"])

    if count == 0:
        print("Your Kraken account has no trade history.")
    else:
        print(f"Your Kraken account has {count} trades:")
        print(trades)
else:
    print(resp["error"])
