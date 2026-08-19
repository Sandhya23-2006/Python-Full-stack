import requests

url="https://catfact.ninja/fact"
response=requests.get(url)
data=response.json()
print(data)

import requests
api_key="0c962a94d697c20c6f88c7136f929819"
city=input("Enter city name: ")
url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
response=requests.get(url)
print("Status Code:",response.status_code)
data=response.json()
if response.status_code==200:
    print()
    print("Weather Information")
    print("--------------")
    print("City:",data["name"])
    print("Temperature:",data["main"]["temp"],"C")
    print("Humidity:",data["weather"][0]["description"])
else:
    print("API Error:",data.get("message"))