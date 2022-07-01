from tkinter import *
import time
import datetime
from plyer import notification
import winsound

window = Tk()
window.geometry("600x500")
window.resizable = (0, 0)
window.configure(background='silver')
window.title("ALARM CLOCK")

date_label = Label(window, fg="#FFF", bg="#232323", font=("Helvetica", 30))
date_label.pack(side=BOTTOM, anchor=W)

time_label = Label(window, bg="#232323", fg="#FFFFFF", font=("Helvetica", 80))
time_label.pack(anchor=CENTER)


def update():
    current_date = time.strftime("%a, %d %b %Y", time.gmtime())
    date_label.config(text=current_date)
    current_time = time.strftime(datetime.datetime.now().strftime('%H:%M:%S'))
    time_label.config(text=current_time)

    if current_time == time_var.get():
        stop_alarm_button.configure(state=NORMAL)
        notification.notify(title="ALARM", message="WAKE UP", app_name="ALARM CLOCK", app_icon=None, timeout=30,
                            toast=False)
        winsound.PlaySound("requirements/mixkit-digital-clock-digital-alarm-buzzer-992.wav",
                           winsound.SND_FILENAME + winsound.SND_LOOP + winsound.SND_ASYNC)

    time_label.after(1000, update)


def set_alarm():
    time_entry.configure(state='disabled')
    alarm_button.configure(state='disabled')

    input_time = time_var.get()
    global exception_label

    try:
        time.strptime(input_time[:8], '%H:%M:%S')

    except ValueError:

        exception_label.configure(text="Wrong Time Format !")
        time_var.set('00:00:00')
        time_entry.configure(state='normal')
        alarm_button.configure(state='normal')

    else:
        if len(input_time) != 8:
            exception_label.configure(text="Wrong Time Format !")
            time_var.set('00:00:00')
            time_entry.configure(state='normal')
            alarm_button.configure(state='normal')

        else:
            exception_label.pack_forget()


time_var = StringVar()
time_var.set('00:00:00')
time_entry = Entry(window, width=50, font="ds-digital 35 bold", justify=CENTER, textvariable=time_var, bg="wheat")
time_entry.pack()

exception_label = Label(window, text="Alarm Not Set !\n Use 24 Hour Format", font="Helvetica 15", bg="red")
exception_label.pack()

alarm_button = Button(window, text="Set Alarm", bg="black", fg="white", font="Helvetica 15", command=set_alarm)
alarm_button.pack(pady=20)


def stop_alarm():
    winsound.PlaySound(None, winsound.SND_FILENAME)


stop_alarm_button = Button(window, text="Stop Alarm", bg="black", fg="white", font="Helvetica 15", command=stop_alarm,
                           state=DISABLED)
stop_alarm_button.pack()

update()
window.mainloop()
winsound.PlaySound(None, winsound.SND_FILENAME)  # closing any sound playing if closes window
