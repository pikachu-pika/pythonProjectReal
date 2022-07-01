from tkinter import *
import time
import datetime


window = Tk()
window.geometry("600x300")
window.resizable=(0, 0)
window.configure(background='#232323')
window.title("CLOCK")


date_label = Label(window, fg ="#FFF", bg ="#232323", font=("Helvetica", 20))
date_label.pack(side=BOTTOM, anchor=W)

time_label = Label(window, text='wake', bg ="#232323", fg ="#FFFFFF", font=("Helvetica", 100))
time_label.pack(anchor=CENTER, fill ="x", expand = 1)


def update():
    current_date = time.strftime("%a, %d %b %Y", time.gmtime())
    date_label.config(text=current_date)
    current_time = time.strftime(datetime.datetime.now().strftime('%H:%M:%S'))
    time_label.config(text=current_time)
    time_label.after(1000, update)


update()
window.mainloop()