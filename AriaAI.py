import datetime
import wikipedia
import wolframalpha
import json
import requests
import pyjokes
def tell_me_a_joke():
    return pyjokes.get_joke
def get_weather(city):
    api_key="8ef61edcf1c576d65d836254e11ea420"
    base_url="https://api.openweathermap.org/data/2.5/weather?"
    complete_url=base_url+"appid="+api_key+"&q=london"
    response = requests.get(complete_url)
    x=response.json()
    if x["cod"]!="404":
        y=x["main"]
        current_temperature = y["temp"]
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        weather = " Temperature in kelvin unit is " + str(current_temperature) + "\n humidity in percentage is " + str(current_humidiy) + "\n description  " + str(weather_description)
        return weather
    else:
        return 'Sorry, city not found'
def search_wikepedia(statement):
    statement =statement.replace("wikipedia", "")
    return wikipedia.summary(statement, sentences=2)
def get_time():
    return datetime.datetime.now().strftime("%H:%M")
def ask_Aria(statement):
    try:
        question=statement
        app_id="WX4A9R-EGQGRH4VKP"
        client = wolframalpha.Client(app_id)
        res = client.query(question)
        answer = next(res.results).text
        return answer
    except:
        return 'Sorry, I do not know that'