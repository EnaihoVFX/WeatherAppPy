import requests
import tkinter

api_key = '30d4741c779ba94c470ca1f63045390a'

def get_weather():
    user_input = location_var.get()
    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&appid={api_key}")

    if weather_data.status_code == 200:
        data = weather_data.json()
        weather = data["weather"][0]["main"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]

        title_label.config(text=f"Weather in {user_input.capitalize()}")
        temp_label.config(text=f"{round(temperature, 1)}°F")
        misc_label.config(text=f"{weather} | Humidity: {humidity}%")
        
        try:
            img = tkinter.PhotoImage(file=f'{weather}.png')
            img_label.config(image=img)
            img_label.image = img
        except Exception as e:
            print(f"Error loading image: {e}")
            img_label.config(image='')
    else:
        title_label.config(text="Location not found")
        temp_label.config(text="")
        misc_label.config(text="")
        img_label.config(image='')

root = tkinter.Tk()
root.geometry("500x700")
root.title("Weather App")

location_var = tkinter.StringVar()
location_label = tkinter.Entry(root, text="Enter a location to find weather", font=("Arial", "20"), textvariable=location_var)
location_label.pack()

get_weather_button = tkinter.Button(root, text="Get Weather", command=get_weather)
get_weather_button.pack(pady=10)

title_label = tkinter.Label(root, text="", font=("Arial", "19"))
title_label.pack(pady="20")

temp_label = tkinter.Label(root, text="", font=("Arial", "30"))
temp_label.pack()

misc_label = tkinter.Label(root, text="", font=("Arial", "10"))
misc_label.pack(pady="5")

img_label = tkinter.Label(root)
img_label.pack()

root.mainloop()
