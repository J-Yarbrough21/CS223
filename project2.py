#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

root = tk.Tk()
root.geometry("900x900")
root.title("Average Test Scores-Lab2")

frame = ttk.Frame(root, padding="10 10 10 10")
frame.pack(fill=tk.BOTH, expand=True)

first_nameLabel = ttk.Label(frame, text="Student First Name: ").grid(
    column=0, row=0, sticky=tk.W
)
first_nameText = tk.StringVar()
first_nameEntry = ttk.Entry(frame, width=200, textvariable=first_nameText).grid(
    column=3, row=0
)

last_nameLabel = ttk.Label(frame, text="Student Last Name: ").grid(
    column=0, row=2, sticky=tk.W
)
last_nameText = tk.StringVar()
last_nameEntry = ttk.Entry(frame, width=200, textvariable=last_nameText).grid(
    column=2, row=2
)

score_oneLabel = ttk.Label(frame, text="Score 1: ").grid(column=0, row=4, sticky=tk.W)
score_oneText = tk.StringVar()
score_oneEntry = ttk.Entry(frame, width=200, textvariable=score_oneText).grid(
    column=2, row=4
)

score_twoLabel = ttk.Label(frame, text="Score 2: ").grid(column=0, row=6, sticky=tk.W)
score_twoText = tk.StringVar()
score_twoEntry = ttk.Entry(frame, width=200, textvariable=score_twoText).grid(
    column=2, row=6
)

score_threeLabel = ttk.Label(frame, text="Score 3: ").grid(column=0, row=8, sticky=tk.W)
score_threeText = tk.StringVar()
score_threeEntry = ttk.Entry(frame, width=200, textvariable=score_threeText).grid(
    column=2, row=8
)

fn_Label = ttk.Label(frame, textvariable=" ", width=200).grid(
    column=0, row=10, sticky=tk.W
)
fn_Entry = ttk.Entry(frame, width=200).grid(column=2, row=10)
fn_Text_str = tk.StringVar()
fn_Label["textvariable"] = fn_Text_str

av_Label = ttk.Label(frame, textvariable=" ", width=200).grid(
    column=0, row=14, sticky=tk.W
)
av_Entry = ttk.Entry(frame, width=200).grid(column=2, row=14)
av_Text_str = tk.StringVar()
av_Label["textvariable"] = av_Text_str

ts_Label = ttk.Label(frame, textvariable=" ", width=200).grid(
    column=0, row=16, sticky=tk.W
)
ts_Entry = ttk.Entry(frame, width=200).grid(column=2, row=16)
ts_Text_str = tk.StringVar()
ts_Label["textvariable"] = ts_Text_str


def click_button1():
    fullname = str(first_nameText.get()) + str(last_nameText.get())
    fn_Text_str.set = fullname


def click_button2():
    root.title("this is the result of button 2")


def click_button3():
    root.destroy()


button1 = ttk.Button(frame, text="Score", command=click_button1)
button1.grid(column=0, row=30)

button2 = ttk.Button(frame, text="Clear", command=None)
button2.grid(column=1, row=30)

button3 = ttk.Button(frame, text="Exit", command=click_button3)
button2.grid(column=2, row=30)

for child in frame.winfo_children():
    child.grid_configure(padx=10, pady=10)

root.mainloop()
