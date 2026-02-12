import requests

def get_weather(city):
    url = f"https://wttr.in/{city}?format=j1"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = data["current_condition"][0]["temp_C"]
        description = data["current_condition"][0]["weatherDesc"][0]["value"]

        print(f"Weather in {city}:")
        print(f"Temperature: {temp}°C")
        print(f"Condition: {description}")
    else:
        print("Failed to fetch weather data")

if __name__ == "__main__":
    city_name = input("Enter city name: ")
    get_weather(city_name)

