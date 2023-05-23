import requests
def Vehicle():
    url= "https://vpic.nhtsa.dot.gov/api/vehicles/getallmanufacturers?format=json"
    response=requests.get(url).json()
    results=response["Results"]
    hasil=[]
    for i in results:
        if i["Country"]=="UNITED KINGDOM (UK)":
            if len(i["VehicleTypes"]) !=0 and i["VehicleTypes"][0]["Name"]== "Passenger Car":
                hasil.append(i["Mfr_CommonName"])
    return hasil
print(Vehicle())