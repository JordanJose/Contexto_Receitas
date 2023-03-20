import geocoder
import requests, json 

base_url = "http://ip-api.com/json/"

def get_ip():
    location = geocoder.ip("me")
    ip_address = location.ip
    ip_url = base_url + ip_address

    response = requests.get(ip_url) 
    resp = response.json() 

    state = resp["region"]
    lat = resp["lat"]
    lon = resp["lon"]

    return state, lat, lon