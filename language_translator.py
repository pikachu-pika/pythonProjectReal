from tkinter import *
from googletrans import Translator

translator = Translator()

root = Tk()
root.title("Translate")
root.geometry("600x500")
root.resizable(0,0)
root.configure(background='#c2f0f0')


Label(text="Text Translator", font="Bold 40", fg="brown").place(x=120, y=10)

my_frame1 = Frame(root)
my_frame1.place(x=0, y=80)

trans_from = StringVar()
trans_to = StringVar()

Label(my_frame1, text="Translate From: ", font="Arial 20", fg="red").grid(row=0, column=0, sticky=W, padx=10, pady=10)
Entry(my_frame1, textvariable=trans_from, font="arial 20", borderwidth=5).grid(row=0, column=1, padx=10, pady=10)

Label(my_frame1, text="Translate To: ", font="Arial 20", fg="red").grid(row=1, column=0, sticky=W, padx=10, pady=10)
Entry(my_frame1, textvariable=trans_to, font="arial 20", borderwidth=5).grid(row=1, column=1, padx=10, pady=10)

my_frame2 = Frame(root)
my_frame2.place(x=0, y=250)

text_to_translate = StringVar()
translated_text = StringVar()

Label(my_frame2, text="To Translate: ", font="Arial 20", fg="blue").grid(row=0, column=0, sticky=W, padx=10,
                                                                         pady=10)
Entry(my_frame2, textvariable=text_to_translate, font="arial 20", borderwidth=5).grid(row=0, column=1, padx=10, pady=10)

Label(my_frame2, text="Translated Text: ", font="Arial 20", fg="blue").grid(row=1, column=0, sticky=W, padx=10, pady=10)
Entry(my_frame2, font="Arial 20", textvariable=translated_text, borderwidth=5).grid(row=1, column=1, padx=10, pady=10)


def translate():
    translation = translator.translate(text_to_translate.get(), src=trans_from.get(), dest=trans_to.get()).text
    translated_text.set(translation)


Button(root, text="Translate", command=translate, fg="brown", bg="wheat", font="arial 30", padx=5, pady=5).place(x=30,
                                                                                                                 y=395)


def reset():
    text_to_translate.set("")
    translated_text.set("")


Button(root, text="Clear ", command=reset, fg="blue", bg="lightblue", font="arial 15", padx=5, pady=5).place(x=280,
                                                                                                             y=390)


def reset_all():
    trans_to.set("")
    trans_from.set("")
    text_to_translate.set("")
    translated_text.set("")


Button(root, text="Reset", command=reset_all, fg="blue", bg="lightblue", font="arial 15", padx=5, pady=5).place(x=280,
                                                                                                                y=440)


def switch():
    temp = trans_from.get()
    trans_from.set(trans_to.get())
    trans_to.set(temp)


Button(root, text="Switch Languages", command=switch, fg="blue", bg="lightblue", font="arial 15", padx=5, pady=5).place(
    x=400, y=415)

root.mainloop()
