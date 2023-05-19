from flask import Flask, render_template
import json
import requests
from geopy import distance
import folium
from dotenv import load_dotenv
import os


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


def draw_map(my_location, coffee_locations):
    m = folium.Map(location=list(my_location)[::-1], zoom_start=12, tiles="Stamen Terrain")

    tooltip = "Click me!"
    for coffee_number, coffee in enumerate(coffee_locations):
        folium.Marker(
            [coffee['longitude'], coffee['latitude']], popup="<i>Mt. Hood Meadows</i>", tooltip=tooltip
        ).add_to(m)

    m.save("templates/index.html")


def fetch_coordinates(apikey, address):
    base_url = "https://geocode-maps.yandex.ru/1.x"
    response = requests.get(base_url, params={
        "geocode": address,
        "apikey": apikey,
        "format": "json",
    })
    response.raise_for_status()
    found_places = response.json()['response']['GeoObjectCollection']['featureMember']

    if not found_places:
        return None

    most_relevant = found_places[0]
    lon, lat = most_relevant['GeoObject']['Point']['pos'].split(" ")
    return lon, lat


def get_coffee_shops_info(my_location):
    with open("coffee.json", "r", encoding='CP1251') as coffee:
        coffee_shops = coffee.read()
    coffee_shops = json.loads(coffee_shops)

    list_coffee_shops = []
    count = 0
    while count < len(coffee_shops):
        coffee_cordinates = tuple(coffee_shops[count]['geoData']['coordinates'])
        dict_coffee_shop = {
            'title': coffee_shops[count]['Name'],
            'distance': distance.distance(reversed(my_location), reversed(coffee_cordinates)).miles,
            'latitude': coffee_cordinates[0],
            'longitude': coffee_cordinates[1]
        }
        list_coffee_shops.append(dict_coffee_shop)
        count += 1
    return list_coffee_shops

from pprint import pprint
if __name__ == '__main__':
    load_dotenv()
    yandex_geo_key = os.getenv('YANDEX_GEO_KEY')
    my_cordinates = fetch_coordinates(yandex_geo_key, input("Где вы находитесь? "))
    print("Ваши координаты: ", my_cordinates)
    min_dict = sorted(get_coffee_shops_info(my_cordinates), key=lambda x: x['distance'])[:5]
    pprint(min_dict)
    draw_map(my_cordinates, min_dict)
    app.run('0.0.0.0')
