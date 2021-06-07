import requests, json
from . import locaion

def queryWeather():
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    CITY = locaion.currentLoaction()
    API_KEY = "fac4889a9371fce77267c589dc4429f2"

    URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY

    try:
        response = requests.get(URL)

        print(response)
        if response.status_code == 200:
            data = response.json()
            main = data['main']
            temperature = main['temp']
            humidity = main['humidity']
            pressure = main['pressure']
            report = data['weather']
            print(f"{CITY:-^30}")
            print(f"Temperature: {temperature}")
            print(f"Humidity: {humidity}")
            print(f"Pressure: {pressure}")
            print(f"Weather Report: {report[0]['description']}")

            weather = f"The weather in {CITY} is {report[0]['description']}"

            return weather
    
    except:
        return ("Error while fetching the data")

print(queryWeather())