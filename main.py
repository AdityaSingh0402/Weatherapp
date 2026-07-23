from weather import Weather

weather = Weather()

print("=" * 40)
print("      WEATHER APPLICATION")
print("=" * 40)

while True:

    city = input("\nEnter city name (or 'exit'): ")

    if city.lower() == "exit":
        print("Goodbye!")
        break

    info = weather.get_weather(city)

    if info:

        print("\nWeather Information")
        print("-" * 30)
        print(f"City        : {info['city']}")
        print(f"Country     : {info['country']}")
        print(f"Temperature : {info['temperature']} °C")
        print(f"Feels Like  : {info['feels_like']} °C")
        print(f"Humidity    : {info['humidity']} %")
        print(f"Pressure    : {info['pressure']} hPa")
        print(f"Wind Speed  : {info['wind_speed']} m/s")
        print(f"Condition   : {info['description']}")

    else:
        print("Could not retrieve weather information.")
