#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk
from xml.dom import pulldom
from tkinter import messagebox

root = tk.Tk()
root.geometry("375x400")
root.title("Average Test Scores-Lab2")

frame = ttk.Frame(root, padding="10 10 10 10")
frame.pack(fill=tk.BOTH, expand=True)

fnameLabel = ttk.Label(frame, text="Student First Name").grid(
    column=0, row=0, sticky=tk.W
)
fnameText = tk.StringVar()
fnameEntry = ttk.Entry(frame, width=25, textvariable=fnameText).grid(column=0, row=2)

lnameLabel = ttk.Label(frame, text="Student Last Name").grid(
    column=1, row=0, sticky=tk.W
)
lnameText = tk.StringVar()
lnameEntry = ttk.Entry(frame, width=25, textvariable=lnameText).grid(column=1, row=2)

score1Label = ttk.Label(frame, text="Score 1").grid(column=0, row=4, sticky=tk.W)
score1Text = tk.StringVar()
score1Entry = ttk.Entry(frame, width=25, textvariable=score1Text).grid(column=1, row=4)

score2Label = ttk.Label(frame, text="Score 2").grid(column=0, row=5, sticky=tk.W)
score2Text = tk.StringVar()
score2Entry = ttk.Entry(frame, width=25, textvariable=score2Text).grid(column=1, row=5)

score3Label = ttk.Label(frame, text="Score 3").grid(column=0, row=6, sticky=tk.W)
score3Text = tk.StringVar()
score3Entry = ttk.Entry(frame, width=25, textvariable=score3Text).grid(column=1, row=6)

fnameText = tk.StringVar()
lnameText = tk.StringVar()
score1Text = tk.StringVar()
score2Text = tk.StringVar()
score3Text = tk.StringVar()

fullname_Label = tk.Label(frame, text=" ").grid(column=0, row=20)

average_Label = tk.Label(frame, text=" ").grid(column=0, row=22)

total_Label = tk.Label(frame, text=" ").grid(column=0, row=24)


def click_button1():
    first = str(fnameText.get())
    last = str(lnameText.get())
    fullname = first + " " + last
    display = "Student Full Name" + str(fullname)
    fullname_Label.grid
    fullname_Label["text"] = display


# fullnameText = fnameText+lnameText
# totalText = score1Entry+score2Entry+score3Entry
# averageText = round(totalText/3)
# display=total and average of scores.


def click_button2():
    root.destroy()


button1 = ttk.Button(frame, text="Calculate", command=None)
button1.grid(column=0, row=30)

button2 = ttk.Button(frame, text="Clear", command=click_button2)
button2.grid(column=1, row=30)

for child in frame.winfo_children():
    child.grid_configure(padx=10, pady=10)

root.mainloop()
