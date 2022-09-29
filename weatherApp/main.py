# Important Module - 
import tkinter as tk
from PIL import Image,ImageTk
import requests



# API key -
# key = '17uoEtuihi6Lsg4hdedT7PUhF4FNgBPD2F'
# https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}


def format_response(weather):
    try:
        city = weather['name']
        condition = weather['weather'][0]['description']
        temp = weather['main']['temp']
        final_str =  'City: %s\nCondition: %s\nTemperature: %s'%(city,condition,temp)
    except:
        final_str = 'There was a problem while reteriving the data from server'
    return final_str


# Get Weather INFO Online -
def get_weather(city):
    weather_Key = '0fecc68658de6ebc1257a738a307885b'
    url = 'https://api.openweathermap.org/data/2.5/weather' 
    params = {'appid': weather_Key,'q':city,'units':'metric'}
    response = requests.get(url,params)
    # print(response.json())
    weather = response.json()
    # print(weather['name'])
    # print(weather['weather'][0]['description'])
    # print(weather['main']['temp'])
    lab_result['text'] = format_response(weather)
    icon_name = weather['weather'][0]['icon']
    open_image(icon_name)

def open_image(icon_name):
    size = int(second_Frame.winfo_height()*0.25)
    img = ImageTk.PhotoImage(Image.open('./img/'+icon_name+'.png').resize((size,size)))
    weather_icon.delete('all')
    weather_icon.create_image(0,0,anchor='nw',image =img)
    weather_icon.image = img

# Initializing the main variable -
root = tk.Tk()


# Title and Layout of window -
root.title("Weather App")
root.geometry("600x500")
root.maxsize(600,500)


# adding Image for App - 
img = Image.open('bg2.jpg')
img = img.resize((600,500),Image.ANTIALIAS)
img_photo = ImageTk.PhotoImage(img)


# adding image as background of window -
bg_label = tk.Label(root,image=img_photo)
bg_label.place(x=0,y=0,width=600,height=500)


# Title Label under image -
heading_title = tk.Label(bg_label,text='Earth including 200K cities!',fg='black',bg='#87a7d4',font=('times new roman',25))
heading_title.place(x=80,y=18,width=450)

# Decorate Frame in Window - 
first_frame = tk.Frame(bg_label,bg='#87a7d4',bd=5)
first_frame.place(x=80,y=60,width=450,height=50)


# Input Text Box -
txt_box = tk.Entry(first_frame,font=('times new roman',25),width=17)
txt_box.grid(row=0,column=0,sticky='w')


# creating button to get result of input text box -
btn = tk.Button(first_frame,text='Click here',fg='green',font=('times new roman',15,'bold'),command=lambda:get_weather(txt_box.get()))
btn.grid(row=0,column=1,padx=22)


# Another Frame -
second_Frame = tk.Frame(bg_label,bg='#87a7d4',bd=5)
second_Frame.place(x=80,y=130,width=450,height=300)


# Creating : result area - 
lab_result = tk.Label(second_Frame,font=40,bg='#ffffff',justify='left',anchor='nw')
lab_result.place(relwidth=1,relheight=1)


weather_icon = tk.Canvas(lab_result,bg='white',bd=0,highlightthickness=0)
weather_icon.place(relx=0.75,rely=0,relwidth=1,relheight=0.50)


# Closing main variable -
root.mainloop()