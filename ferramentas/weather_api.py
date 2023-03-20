import requests, json 

api_key = "8f07ff954fb086ad185e46b3104fbaaa"
base_url = "https://api.openweathermap.org/data/2.5/weather?"

def format_weather(weather):
    if weather in ["Drizzle", "Thunderstorm", "Rain"]:
            return "chuva"
    elif weather == "Snow":
        return "neve"

    elif weather == "Clear":
        return "ceu claro"

    elif weather == "Clouds":
        return "nuvens"
    else:
        return "outros"

def format_temp(temp):
    if temp < 20:
        return "frio"
    if temp >= 20 and temp < 30:
        return "normal"
    if temp >= 30:
        return "quente"

def get_weather(lat, lon):

    complete_url = base_url + "lat=" + str(lat) + "&lon=" + str(lon) + "&appid=" + api_key

    response = requests.get(complete_url) 
    resp = response.json() 

    if resp["cod"] != "404": 
        weather = resp["weather"][0]["main"]

        temp = resp["main"]["temp"]
        
        temp = int(temp - 273.15)

        weather = format_weather(weather)
        temp = format_temp(temp)
        
        return weather, temp    
    else:   
        return 0

# print(get_weather(-3.1032, -60.0288))