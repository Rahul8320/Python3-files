import requests
import time 

city = str(input("Enter Your city : "))
api = "https://api.openweathermap.org/data/2.5/weather?q="+city +"&appid=d2d5059c5a5dbed0c83094d11c27dc7c"
json_data = requests.get(api).json()
condition = json_data['weather'][0]['main']
temp = int(json_data['main']['temp'] - 273.15)
max_temp = int(json_data['main']['temp_max'] - 273.15)
min_temp = int(json_data['main']['temp_min'] - 273.15)
pressure = json_data['main']['pressure']
humidity = json_data['main']['humidity']
wind = json_data['wind']['speed']
sunrise = time.strftime("%I:%M:%S", time.gmtime(
    json_data['sys']['sunrise'] + 19800))
sunset = time.strftime("%I:%M:%S", time.gmtime(
    json_data['sys']['sunset'] + 19800))
local_time = time.strftime("%I:%M:%S", time.localtime())

weather_info = condition + "\n" + str(temp) + "°C"
weather_data = "\nMax Temp: "+str(max_temp) + "°C\nMin Temp : "+str(min_temp) + "°C\nPressure : "+str(pressure) + "hpa\nHumidity : "+str(
    humidity) + "%\nWind : "+str(wind) + "mph\nSunrise : "+str(sunrise) + "\nSunset : "+str(sunset)  # +"\nLocaltime : "+str(local_time)
print(weather_info+"\n"+weather_data)
print(local_time)
