import requests

url = "https://api.openweathermap.org/data/2.5/weather?q=bandung&appid=0af7650b00321f8081a8a9ad3a838f51&lang=id&units=metric"

payload= {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

# print('tipe response: ',type(response))
response_json = response.json()

print("hasil: ", response_json)

#type: string
# print(type(response.txt))
# type: dict
print(type(response.json()))

desc_weather = response_json["weather"][0]["description"]
humidity = response_json["main"]["humidity"]
print('kondisi cuaca: ',desc_weather)
print('kelembaban:',humidity)
print(response)


