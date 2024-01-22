import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()

def get_current_weather(city = "Lagos"):
    request_url = f'https://api.openweathermap.org/data/2.5/weather?&appid={os.getenv("API_KEY")}&q={city}&units=metric'

    weather_data = requests.get(request_url).json()

    # pprint(weather_data)

    # print(f"\nCurrent weather for {weather_data["name"]}\n")
    # print(f"\nThe temp is,  {weather_data["main"]["temp"]}\n")
    # print(f"\nFeels like {weather_data["main"]["feels_like"]} and {weather_data["weather"][0]["description"]}\n")
    return weather_data

if __name__ == "__main__": 
    print("\n *** Get current weather conditons ***\n")
    city = input("\n Please enter a city name\n")

    weather_data = get_current_weather(city)

    pprint(weather_data)