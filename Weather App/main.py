import tkinter as tk 
import requests
import time

def getWeather(canvas):
    city = textfield.get()
    api = "http://api.openweathermap.org/data/2.5/weather?q=" + \
        city + "&appid=d2d5059c5a5dbed0c83094d11c27dc7c"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise'] + 19800))
    sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset'] + 19800))
    # local_time = time.strftime("%I:%M:%S", time.localtime())

    weather_info = condition +"\n" +str(temp) + "°C"
    weather_data = "\nMax Temp: "+str(max_temp) + "°C\nMin Temp : "+str(min_temp) + "°C\nPressure : "+str(pressure) + "hpa\nHumidity : "+str(humidity) + "%\nWind : "+str(wind) + "mph\nSunrise : "+str(sunrise) + "\nSunset : "+str(sunset) #+"\nLocaltime : "+str(local_time)
    print(weather_info+"\n"+weather_data)
    
    label1.config(text= weather_info)
    label2.config(text= weather_data)



canvas = tk.Tk()
canvas.geometry("700x700")  # default geometry of root window
canvas.title("Weather Applications") # default title of root window
 
f = ("poppins",15,"bold")
t = ("poppins",35,"bold")

textfield = tk.Entry(canvas,justify='center',font=t)  # make a textfield input
textfield.pack(pady = 20)
textfield.focus()  #  focus the textfield input as we can directly type our location query after enter the application
textfield.bind('<Return>', getWeather)

label1 = tk.Label(canvas,font=t)
label1.pack()
label2 = tk.Label(canvas,font=f)
label2.pack()

canvas.mainloop()
