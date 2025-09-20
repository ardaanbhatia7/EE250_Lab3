import requests

# WeatherAPI key
WEATHER_API_KEY = "51f518b4283543e784b40556252009"  # TODO: Replace with your own WeatherAPI key

def get_weather(city):
    # TODO: Build the API request URL using the base API endpoint, the API key, and the city name provided by the user
     base_url = "http://api.weatherapi.com/v1/current.json"
     url = f"{base_url}?key={WEATHER_API_KEY}&q={city}&aqi=no"
    # TODO: Make the HTTP request to fetch weather data using the 'requests' library.
     response = requests.get(url)
    # TODO: Handle HTTP status codes:
    # - Check if the status code is 200 (OK), meaning the request was successful.
    # - If not 200, handle common errors like 400 (Bad Request), 401 (Unauthorized), 404 (Not Found), and any other relevant codes.
    
     if response.status_code == 200:
        # TODO: Parse the JSON data returned by the API. Extract and process the following information:
        # - Current temperature in Fahrenheit
        # - The "feels like" temperature
        # - Weather condition (e.g., sunny, cloudy, rainy)
        # - Humidity percentage
        # - Wind speed and direction
        # - Atmospheric pressure in mb
        # - UV Index value
        # - Cloud cover percentage
        # - Visibility in miles
        data = response.json()
        current = data["current"]

        # Extract information
        temperature_f = current["temp_f"]
        feelslike_f = current["feelslike_f"]
        condition = current["condition"]["text"]
        humidity = current["humidity"]
        wind_mph = current["wind_mph"]
        wind_dir = current["wind_dir"]
        pressure_mb = current["pressure_mb"]
        uv_index = current["uv"]
        cloud_cover = current["cloud"]
        visibility_miles = current["vis_miles"]
    
        # TODO: Display the extracted weather information in a well-formatted manner.
        print(f"Weather data for {city}...")
        print(f"\nWeather data for {city}:")
        print(f"  Temperature: {temperature_f}°F (Feels like {feelslike_f}°F)")
        print(f"  Condition:   {condition}")
        print(f"  Humidity:    {humidity}%")
        print(f"  Wind:        {wind_mph} mph {wind_dir}")
        print(f"  Pressure:    {pressure_mb} mb")
        print(f"  UV Index:    {uv_index}")
        print(f"  Cloud Cover: {cloud_cover}%")
        print(f"  Visibility:  {visibility_miles} miles")

     elif response.status_code == 400:
        print("Error 400: Bad Request — invalid city name or parameters.")
     elif response.status_code == 401:
        print("Error 401: Unauthorized — check your API key.")
     elif response.status_code == 404:
        print("Error 404: City not found.")
     else:
        # TODO: Implement error handling for common status codes. Provide meaningful error messages based on the status code.
        print(f"Error: {response.status_code}. Something went wrong.")

if __name__ == '__main__':
    # TODO: Prompt the user to input a city name.
    city = input("Enter a city: ") 
    # TODO: Call the 'get_weather' function with the city name provided by the user.
    get_weather(city)
    pass
