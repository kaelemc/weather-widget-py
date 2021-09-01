import requests
import json
import geocoder

# api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}

api_key = "" # api key here
base_url = "http://api.openweathermap.org/data/2.5/"

def callWeatherAPI(latitude, longitude):
    api_url = "{url}weather?lat={_lat}&lon={_lon}&appid={_api_key}&units=metric".format(url=base_url, _lat=latitude, _lon=longitude, _api_key=api_key)
    
    print(api_url)  # so I can open the link in my browser and analyze the HTTP response headers

    response = requests.get(api_url)

    # if http response code is not 200 (OK) then an error has occured and return None type
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

def getWeather():
    location = geocoder.ip('me')
    print(location.latlng)
    weatherDict = callWeatherAPI(location.latlng[0], location.latlng[1])

    if weatherDict is not None:
        return [ weatherDict['name'], weatherDict['weather'][0]['description'], weatherDict['main']['temp'], weatherDict['main']['humidity']] 
    else:
        return None