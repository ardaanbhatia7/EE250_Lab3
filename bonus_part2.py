import requests
import time

url = "https://official-joke-api.appspot.com/random_joke"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("😂 Here's a random joke (using REST APIs) " + "(joke id: " + str(data["id"]) + "): ")
    print(data["setup"])
    
    #sleep for a bit - so user can think 
    time.sleep(3)

    print(data["punchline"])
else:
    print("Error:", response.status_code)
