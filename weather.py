import requests
import json
import geocoder

# grab config from json file for security when commiting and ease of config
config_file = open("config.json", "r")

config_dict = json.loads(config_file.read())
# close file
config_file.close()

# set true to show debugging hints in console
DEBUG_FLAG = config_dict["debug"]

# api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
api_key = config_dict["api_key"]
base_url = "http://api.openweathermap.org/data/2.5/"

def callWeatherAPI(latitude, longitude):
    api_url = "{url}weather?lat={_lat}&lon={_lon}&appid={_api_key}&units=metric".format(url=base_url, _lat=latitude, _lon=longitude, _api_key=api_key)
    
    if DEBUG_FLAG: print(api_url)  # so I can open the link in my browser and analyze the HTTP response headers

    response = requests.get(api_url)

    # if http response code is not 200 (OK) then an error has occured and return None type
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

def getWeather():
    location = geocoder.ip('me')
    if DEBUG_FLAG: print(location.latlng)
    weather_dict = callWeatherAPI(location.latlng[0], location.latlng[1])

    if weather_dict is not None:
        return [ weather_dict['name'], weather_dict['weather'][0]['description'], weather_dict['main']['temp'], weather_dict['main']['humidity'], weather_dict['weather'][0]['icon']] 
    else:
        return None