import requests

def Weather_controller(location):
    url = f"http://api.weatherapi.com/v1/current.json?key=3adbea022f0d4d778f1230311242306&q={location}"
    req = requests.get(url)
    temp = req.json()["current"]["temp_c"]
    print(temp)
location = input("Enter location: ")
Weather_controller(location)

#this is very newwwwww
print(temp)
