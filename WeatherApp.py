from tkinter import *
from tkinter import messagebox
from configparser import ConfigParser
import requests

url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

config_file = "config.ini"
config = ConfigParser()
config.read(config_file)
api_key = "ec71b084976d51542238c3978192ffc3"

def get_weather(city):
    result = requests.get(url.format(city, api_key))
    if result:
        json = result.json()
        city = json["name"]
        country = json["sys"]["country"]
        temp_kelvin = json["main"]["temp"]
        temp_celsius = temp_kelvin - 273.15
        temp_fahrenheit = (temp_kelvin - 273.15) * 9 / 5 + 32 
        icon = json["weather"][0]["icon"]
        weather = json ["weather"][0]["main"]
        description = json ["weather"][0]["description"]
        longitude = json["coord"]["lon"]
        latitude = json["coord"]["lat"]
        pressure = json["main"]["pressure"]
        humidity = json["main"]["humidity"]
        final = (city, country, temp_celsius, temp_fahrenheit, icon, weather, description, longitude, latitude, pressure,humidity)
        print(final)
        return final
    else:
        return None

def search():
    city = city_text.get()
    weather = get_weather(city)
    if weather:
        location_lbl["text"] = "{}, {}".format(weather[0], weather[1])
        image["bitmap"] = "weather_icons/{}.png".format(weather[4])
        temp_lbl["text"] = "{:.2f}°C, {:.2f}°f".format(weather[2], weather[3])
        weather_lbl["text"] = weather[5] 
        weatherDesc_lbl["text"] = weather[6]
    else:
        messagebox.showerror("Error", "Cannot find city {}".format(city))
        
def Advanced_search():
    city = city_text.get()
    weather = get_weather(city)
    if weather:
        location_lbl["text"] = "{}, {}".format(weather[0], weather[1])
        coordinates_lbl["text"] = "Longitude: {:.2f}, Latitude: {:.2f}".format(weather[7], weather[8])
        temp_lbl["text"] = "{:.2f}°C, {:.2f}°f".format(weather[2], weather[3])
        pressure_lbl["text"] = "Pressure: {:.2f}".format(weather[9])
        humidity_lbl["text"] = "Humidity: {:.2f}".format(weather[10])
        weather_lbl["text"] = weather[5] 
        weatherDesc_lbl["text"] = weather[6]
    else:
        messagebox.showerror("Error", "Cannot find city {}".format(city))

app = Tk()
app.title("Weather App")
app.geometry("700x350")

city_text = StringVar()
city_entry = Entry(app, textvariable=city_text)
city_entry.pack()

search_btn1 = Button(app, text="Search weather", width=12, command=search)
search_btn1.pack()

search_btn2 = Button(app, text="Advanced Search", width=12, command=Advanced_search)
search_btn2.pack()

location_lbl = Label(app, text="Location", font=("bold, 20"))
location_lbl.pack()

image = Label(app, bitmap="")
image.pack()

temp_lbl = Label(app, text="")
temp_lbl.pack()

weather_lbl = Label(app, text="")
weather_lbl.pack()

weatherDesc_lbl = Label(app, text="")
weatherDesc_lbl.pack()

pressure_lbl = Label(app, text="")
pressure_lbl.pack()

humidity_lbl = Label(app, text="")
humidity_lbl.pack()

windSpeed_lbl = Label(app, text="")
windSpeed_lbl.pack()

coordinates_lbl = Label(app, text="")
coordinates_lbl.pack()

app.mainloop()

#Need to comment , add styling and work on the advanced_search