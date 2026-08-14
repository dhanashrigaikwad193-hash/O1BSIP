import requests

city = input("Enter city name: ")

if city.strip() == "":
    print("City name cannot be empty.")

else:
    api_key = "YOUR_API_KEY"
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params, timeout=10)

        if response.status_code == 200:
            data = response.json()

            temperature_c = data["main"]["temp"]
            temperature_f = (temperature_c * 9 / 5) + 32
            humidity = data["main"]["humidity"]
            condition = data["weather"][0]["description"]
            wind_speed = data["wind"]["speed"]

            print("\n--- Current Weather ---")
            print("City:", city)
            print("Temperature:", temperature_c, "°C")
            print("Temperature:", temperature_f, "°F")
            print("Humidity:", humidity, "%")
            print("Condition:", condition)
            print("Wind Speed:", wind_speed, "m/s")

        elif response.status_code == 404:
            print("City not found.")

        elif response.status_code == 401:
            print("Invalid API key.")

        else:
            print("Unable to fetch weather data.")

    except requests.exceptions.Timeout:
        print("Request timed out. Please try again.")

    except requests.exceptions.RequestException:
        print("Network error. Please check your internet connection.")