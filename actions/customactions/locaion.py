import requests

def currentLoaction():
    resp = requests.get('https://ipinfo.io/103.99.205.122?token=dc5b64410200cf')
    data = resp.json()
    city = data['city']
    print(city)
    return city