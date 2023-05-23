import requests
def OpenWeather(cities):
    Domain_Name="https://api.openweathermap.org"
    Path_Name="/data/2.5/weather?"
    # QUERY INPUT
    city_input="q="
    API_id="&appid=0af7650b00321f8081a8a9ad3a838f51"
    unit="&units="
    bahasa="&lang="
    for i in cities:
        url=Domain_Name+Path_Name+city_input+i[0]+API_id+unit+i[1]+bahasa+i[2]
        response=requests.request("GET",url)
        response_json=response.json()
        city_name=response_json["name"]
        temperature=response_json["main"]["temp"]
        temperature_feel_like=response_json["main"]["feels_like"]
        desc_weather=response_json["weather"][0]["description"]
        print(city_name,"bersuhu",temperature,"terasa seperti",temperature_feel_like,"berkondisi",desc_weather)
OpenWeather([["sleman","metric","id"],["bantul","metric","id"],["wates","metric","id"]])
