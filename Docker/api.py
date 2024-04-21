from datetime import datetime
from flask import Flask, request, Response, render_template
import requests
import random
import openmeteo_requests
import requests_cache
from retry_requests import retry
from unidecode import unidecode
import os

app = Flask(__name__, template_folder="./static/templates/")

import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

stock_apikey = os.environ['alphavantageKey']
api_hostname = os.environ['hostname']
pfHostname = os.environ['fullHostname']
serverPort = os.environ['serverPort']
fullHostname = f'{pfHostname}:{serverPort}'

@app.route("/homepage/")
def homepage():
    code = render_template("cisco.xml", hostname=fullHostname)
    return Response(code, mimetype='text/xml')

@app.route("/scrOff/")
def scrOff():
    code = render_template("scr-off.xml")
    return Response(code, mimetype='text/xml')

@app.route("/getStock/")
def getStock():
    code = render_template("get_stock.xml", hostname=fullHostname)
    return Response(code, mimetype='text/xml')

@app.route("/getWeather/")
def getWeather():
    code = render_template("geocode_weather.xml",hostname=fullHostname)
    return Response(code, mimetype='text/xml')

@app.route("/info/")
def getInfo():
    code = render_template("info.xml")
    return Response(code, mimetype='text/xml')

@app.route("/playRps/")
def playRps():
    code = render_template("rps.xml",hostname=fullHostname)
    return Response(code, mimetype='text/xml')

@app.route("/getAqi/")
def getAqi():
    code = render_template("geocode_aqi.xml",hostname=fullHostname)
    return Response(code, mimetype='text/xml')

@app.route("/getGamesList/")
def getGamesList():
    code = render_template("games.xml",hostname=fullHostname)
    return Response(code, mimetype='text/xml')

@app.route("/getEnvApps/")
def getEnvApps():
    code = render_template("environmental.xml",hostname=fullHostname)
    return Response(code, mimetype='text/xml')

# backend calls

@app.route("/stock-price/")
def get_stock():
    nsymb = request.args.get("symbol")
    out = requests.get(f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={nsymb}&apikey={stock_apikey}")
    out = out.json()
    price = round(float(out['Global Quote']['05. price']), 2)
    change = round(float(out['Global Quote']['09. change']), 2)
    change_percent = out['Global Quote']['10. change percent']

    if change > 0:
        up_or_down = "UP ^"
    else:
        up_or_down = "DOWN"

    sResp = render_template("stock_value.xml", symbol=nsymb.upper(), price=price,
                            change=change, up_or_down=up_or_down, change_percent=change_percent)
    return Response(sResp, mimetype='text/xml')

@app.route("/geocode-aqi/")
def geocode_aqi():
    try:
        name = request.args.get("name").upper()
        out = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={name}&count=10&language=en&format=json")
        out = out.json()
        cities_data = out['results']
        city_info_list = [{'name': city['name'], 'admin1': city.get('admin1', ''), 'latitude': city['latitude'],
                           'longitude': city['longitude'], 'country_code': city['country_code']} for city in cities_data]

        output = f"<CiscoIPPhoneMenu>\n"
        output += f"<Title>Results for your search</Title>\n"
        for city_info in city_info_list:
            city_name = city_info['name']
            city_name = unidecode(city_name)
            city_region = city_info['admin1']
            output += f"<MenuItem>"
            output += f"  <Name>{city_name}, {city_info['admin1']}, {city_info['country_code']}</Name>"
            city_name = city_name.replace(" ", "_")
            city_region = city_region.replace(" ", "_")
            output += f"  <URL>{fullHostname}/air-quality/?latitude={city_info['latitude']}&amp;longtitude={city_info['longitude']}&amp;name={city_name}&amp;region={city_region}&amp;country={city_info['country_code']}</URL>"
            output += f"</MenuItem>"
        output += f"</CiscoIPPhoneMenu>"

        return Response(output, mimetype='text/xml')
    except:
        return Response(render_template("no_results.xml"), mimetype='text/xml')
    # return out, 200

@app.route("/geocode-weather/")
def geocode_weather():
    try:
        name = request.args.get("name").upper()
        out = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={name}&count=10&language=en&format=json")
        out = out.json()
        cities_data = out['results']
        city_info_list = [{'name': city['name'], 'admin1': city.get('admin1', ''), 'latitude': city['latitude'],
                        'longitude': city['longitude'], 'country_code': city['country_code']} for city in cities_data]

        output = f"<CiscoIPPhoneMenu>\n"
        output += f"<Title>Results for your search</Title>\n"
        for city_info in city_info_list:
            city_name = city_info['name']
            city_name = unidecode(city_name)
            city_region = city_info['admin1']
            output += f"<MenuItem>"
            output += f"  <Name>{city_name}, {city_info['admin1']}, {city_info['country_code']}</Name>"
            city_name = city_name.replace(" ", "_")
            city_region = city_region.replace(" ", "_")
            output += f"  <URL>{fullHostname}/weather/?latitude={city_info['latitude']}&amp;longtitude={city_info['longitude']}&amp;name={city_name}&amp;region={city_region}&amp;country={city_info['country_code']}</URL>"
            output += f"</MenuItem>"
        output += f"</CiscoIPPhoneMenu>"

        return Response(output, mimetype='text/xml')
    except:
        return Response(render_template("no_results.xml"), mimetype='text/xml')
    # return out, 200

@app.route("/air-quality/")
def get_air_quality():    
    latitude = float(request.args.get("latitude"))
    longtitude = float(request.args.get("longtitude"))
    name = request.args.get("name").replace("_", " ")
    region = request.args.get("region").replace("_", " ")
    country = request.args.get("country")
    out = requests.get(f"https://air-quality-api.open-meteo.com/v1/air-quality?latitude={latitude}&longitude={longtitude}&current=us_aqi,dust")
    out = out.json()
    current = out['current']
    dust = current['dust']
    air_quality = current['us_aqi']
    date = (f'{datetime.now().year}-{datetime.now().month}-{datetime.now().day} ' +
            f'{datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}')

    aqResp = render_template("air_quality.xml", city=name, region=region, country=country,
                          dust=dust, air_quality=air_quality, last_update=date)

    return Response(aqResp, mimetype='text/xml')
    # return out, 200

@app.route("/weather/")
def weather():
    latitude = float(request.args.get("latitude"))
    longtitude = float(request.args.get("longtitude"))
    name = request.args.get("name").replace("_", " ")
    region = request.args.get("region").replace("_", " ")
    country = request.args.get("country")
    # Setup the Open-Meteo backend client with cache and retry on error
    cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
    retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
    openmeteo = openmeteo_requests.Client(session = retry_session)
    # Make sure all required weather variables are listed here
	# The order of variables in hourly or daily is important to assign them correctly below
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
		"latitude": latitude,
		"longitude": longtitude,
		"current": ["temperature_2m", "precipitation", "wind_speed_10m", "wind_gusts_10m", "relative_humidity_2m"],
		"hourly": ["temperature_2m", "precipitation_probability", "precipitation", "wind_speed_10m", "wind_gusts_10m"],
		"wind_speed_unit": "ms",
		"timezone": "auto",
		"forecast_days": 1
	}
    responses = openmeteo.weather_api(url, params=params)
    response = responses[0]
    current = response.Current()
    current_temperature_2m = current.Variables(0).Value()
    current_precipitation = current.Variables(1).Value()
    current_wind_speed_10m = current.Variables(2).Value()
    current_wind_gusts_10m = current.Variables(3).Value()
    current_relative_humidity_2m = current.Variables(4).Value()
    date = (f'{datetime.now().year}-{datetime.now().month}-{datetime.now().day} '+
            f'{datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}')

    wResp = render_template("weather.xml", city=name, region=region, country=country,
                          temperature=round(current_temperature_2m, 2), precipitation=current_precipitation,
                          w_speed=round(current_wind_speed_10m, 2), wg_speed=round(current_wind_gusts_10m, 2),
                          humidity=round(current_relative_humidity_2m, 2), last_update=date)

    return Response(wResp, mimetype='text/xml')

@app.route("/rps/")
def rock_paper_scissors():
    user_input = request.args.get("user_input")
    global computer
    possible = ['rock','paper','scissors']
    computer = random.choice(possible)

    if user_input == 'rock' and computer == 'paper':
        lWin = "You loose!"
    elif user_input == 'rock' and computer == 'scissors':
        lWin = "You win!"
    elif user_input == 'rock' and computer == 'rock':
        lWin = "Tie"
    elif user_input == 'paper' and computer == 'rock':
        lWin = "You win!"
    elif user_input == 'paper' and computer == 'scissors':
        lWin = "You loose!"
    elif user_input == 'paper' and computer == 'paper':
        lWin = "Tie"
    elif user_input == 'scissors' and computer == 'rock':
        lWin = "You loose!"
    elif user_input == 'scissors' and computer == 'paper':
        lWin = "You win"
    if user_input == 'scissors' and computer == 'scissors':
        lWin = "Tie"

    rpsResp = render_template("rps_out.xml", computer=computer.capitalize(), result=lWin, hostname=fullHostname)

    return Response(rpsResp, mimetype='text/xml')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
