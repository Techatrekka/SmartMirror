from tkinter import*
from fetchdata import*
import time, tkinter as tk

firstTime = True

root = tk.Tk()
root.geometry("600x1000")
root.configure(bg = "black")
#root.attributes("-fullscreen", True)
frame = Frame(root)
frame.pack()

topleftFrame = Frame(root)
topleftFrame.pack(side=TOP, anchor="nw")
data = fetchdata.getWeatherUpdate()
temp = data[0],"\N{DEGREE SIGN}"+"C"
temperature = Label(topleftFrame, text = temp,
               fg ="white", bg="black", font=("Helvetica",40))
temperature.pack(fill=tk.BOTH, expand = True)

pressureReading = data[1], "hPa"

humidityReading = data[2],"%"

humpres = str(pressureReading).replace('(','').replace(')','').replace('\'','').replace(',','').replace(' ','')+ ", "+ str(humidityReading).replace('(','').replace(')','').replace('\'','').replace(',','').replace(' ','')

humidity = Label(topleftFrame, text = str(humpres),
               fg ="white", bg="black", font=("Helvetica",20))
humidity.pack(fill=tk.BOTH, expand = True)

description = Label(topleftFrame, text = data[3],
               fg ="white", bg="black", font=("Helvetica",15))
description.pack(fill=tk.BOTH, expand = True)

root.title("Mirror")
if firstTime:
    firstTime = False
else:
    time.sleep(30)

root.mainloop()
