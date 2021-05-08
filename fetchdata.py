import requests, json

class fetchdata:    

    def getWeatherUpdate():
        openweatherAPIkey = "251ef3dcc8d484ad7170cb8fe5c4b8f1"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        city_name = "Cratloe"
        complete_url = base_url + "appid=" + openweatherAPIkey + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()
        
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            current_temperature = round(current_temperature - 273.15,1)
            data = [current_temperature, current_pressure,
                    current_humidity, weather_description]
            
            return data
  
        else:
            print(" City Not Found ")


fetchdata.getWeatherUpdate()
