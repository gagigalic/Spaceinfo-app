import json
import tkinter
from tkinter import *
import requests
from PIL import ImageTk,Image

endpoint_location = "http://api.open-notify.org/iss-now.json"
endpoint_number = "http://api.open-notify.org/astros.json"



def List_of_people():
    response_list = requests.get(endpoint_number)
    list_of_people = response_list.json()["people"]
    name_list = [entry["name"] for entry in list_of_people]
    names_as_string = '\n'.join(name_list)
    answer_people.config(text = names_as_string)

def CurrentLocation():
    response_location = requests.get(endpoint_location)
    latitude = response_location.json()["iss_position"]["latitude"]
    longitude = response_location.json()["iss_position"]["longitude"]

    answer_location.config(text = f"Lat: {latitude}, Lon: {longitude}")


def NumberPeople():
    response_number = requests.get(endpoint_number)
    number = response_number.json()["number"]

    answer_number.config(text = f"There are {number} people in space right now!")
    window.after(2000, new)

def new():
    window.destroy()
    global windows2
    windows2 = Tk()
    windows2.title("Space info")
    windows2.config(padx=25, pady=25, bg="#1D5B79")





    text_peoples = Label(text="Do you want names this peoples?", font=("Ariel", 20), bg="#1D5B79", fg="#F5F5F5",
                         pady=15)
    text_peoples.grid(column=0, row=0, columnspan=2)

    yes_peoples = Button(text="Yes", font=20, width=15, bg="#1D5B79", fg="#F5F5F5", command = List_of_people)
    yes_peoples.grid(column=0, row=1)

    no_peoples = Button(text="No", font=20, width=15, bg="#1D5B79", fg="#F5F5F5", command=Close2)
    no_peoples.grid(column=1, row=1)

    global answer_people
    answer_people = Label(text=" ", font=("Ariel", 20), bg="#1D5B79", fg="#F5F5F5")
    answer_people.grid(column=0, row=2, columnspan=2)




def Close():
    window.destroy()

def Close2():
    windows2.destroy()
    


window = Tk()
window.title("Space info")
window.config(padx=25, pady=25, bg ="#1D5B79" )


title_label=Label(text="Space info ", font = ("Ariel", 30, "bold"), bg = "#1D5B79", fg = "#F5F5F5")
title_label.grid(column = 0, row = 0, columnspan = 2)

text_Location= Label(text = "Do you want to now ISS Current Location?", font = ("Ariel", 20),  bg = "#1D5B79", fg = "#F5F5F5", pady =15)
text_Location.grid(column = 0, row = 1, columnspan = 2)

yes_location = Button(text = "Yes", font = 20, width = 15,  bg = "#1D5B79", fg = "#F5F5F5", command = CurrentLocation)
yes_location.grid(column = 0, row = 2)

no_location = Button(text = "No", font = 20, width = 15,  bg = "#1D5B79", fg = "#F5F5F5", command = Close)
no_location.grid(column = 1, row = 2)

answer_location= Label(text = " ", font = ("Ariel", 20),  bg = "#1D5B79", fg = "#F5F5F5")
answer_location.grid(column = 0, row = 3, columnspan = 2)

text_number= Label(text = "How many people are there in the space?", font = ("Ariel", 20),  bg = "#1D5B79", fg = "#F5F5F5", pady= 15)
text_number.grid(column = 0, row = 4, columnspan = 2)

yes_number = Button(text = "Yes", font = 20, width = 15,  bg = "#1D5B79", fg = "#F5F5F5", command = NumberPeople)
yes_number.grid(column = 0, row = 5)

no_number = Button(text = "No", font = 20, width = 15,  bg = "#1D5B79", fg = "#F5F5F5", command = Close)
no_number.grid(column = 1, row = 5)

answer_number= Label(text = " ", font = ("Ariel", 20),  bg = "#1D5B79", fg = "#F5F5F5")
answer_number.grid(column = 0, row = 6, columnspan = 2)






window.mainloop()