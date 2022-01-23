#!/usr/bin/env python3
import tkinter as tk
from tkinter import W, ttk
from tkinter import messagebox
from turtle import left

root = tk.Tk()
root.geometry("700x500")
root.title("Average Test Scores-Lab2")

frame = ttk.Frame(root, padding="10 10 10 10")
frame.pack(fill=tk.BOTH, expand=True)

first_nameLabel = ttk.Label(frame, text="Student First Name: ").grid(
    column=0, row=0, sticky=tk.W
)
first_nameText = tk.StringVar()
first_nameEntry = ttk.Entry(frame, width=25, textvariable=first_nameText).grid(
    column=1, row=0
)

last_nameLabel = ttk.Label(frame, text="Student Last Name: ").grid(
    column=0, row=2, sticky=tk.W
)
last_nameText = tk.StringVar()
last_nameEntry = ttk.Entry(frame, width=25, textvariable=last_nameText).grid(
    column=1, row=2
)

score_oneLabel = ttk.Label(frame, text="Score 1: ").grid(column=0, row=4, sticky=tk.W)
score_oneText = tk.StringVar()
score_oneEntry = ttk.Entry(frame, width=25, textvariable=score_oneText).grid(
    column=1, row=4
)

score_twoLabel = ttk.Label(frame, text="Score 2: ").grid(column=0, row=6, sticky=tk.W)
score_twoText = tk.StringVar()
score_twoEntry = ttk.Entry(frame, width=25, textvariable=score_twoText).grid(
    column=1, row=6
)

score_threeLabel = ttk.Label(frame, text="Score 3: ").grid(column=0, row=8, sticky=tk.W)
score_threeText = tk.StringVar()
score_threeEntry = ttk.Entry(frame, width=25, textvariable=score_threeText).grid(
    column=1, row=8
)


fn_Text_str = tk.StringVar()
fn_Text_str.set("")
fn_Label = ttk.Label(frame, text="Students Full Name: ").grid(
    column=0, row=12, sticky=tk.W
)
full_nameEntry = ttk.Entry(frame, text=fn_Text_str, state="readonly").grid(
    column=1, row=12, sticky=tk.E
)

avg_Text_str = tk.StringVar()
avg_Text_str.set("")
avg_scoreLabel = ttk.Label(frame, text="Average Test Score: ").grid(column=0, row=14)
avg_Entry = ttk.Entry(frame, text=avg_Text_str, state="readonly").grid(
    column=1, row=14, sticky=tk.E
)

total_Text_str = tk.StringVar()
total_Text_str.set("")
avg_scoreLabel = ttk.Label(frame, text="Total Test Score: ").grid(column=0, row=16)
total_Entry = ttk.Entry(frame, text=total_Text_str, state="readonly").grid(
    column=1, row=16, sticky=tk.E
)


def get_scores():
    # Setting the retrieved values for the scores as elements in a list.
    tmp_scores = [score_oneText.get(), score_twoText.get(), score_threeText.get()]
    # returning a list comprehension where the strings are converted to floats.
    return [float(x) for x in tmp_scores]


def total_score():
    # returning the sum of the scores in the list.
    return sum(get_scores())


def avg_score():
    # returning the average of the scores in the list
    return sum(get_scores()) / len(get_scores())


def clk_score():
    fn_Text_str.set(first_nameText.get() + " " + last_nameText.get())
    avg_Text_str.set("{:.2f}".format(avg_score()))
    total_Text_str.set("{:.2f}".format(total_score()))


def clk_clear():
    first_nameText.set("")
    last_nameText.set("")
    score_oneText.set("")
    score_twoText.set("")
    score_threeText.set("")
    fn_Text_str.set("")
    avg_Text_str.set("")
    total_Text_str.set("")


def click_button3():
    root.destroy()


button1 = ttk.Button(frame, text="Score", command=clk_score)
button1.grid(column=0, row=30)

button2 = ttk.Button(frame, text="Clear", command=clk_clear)
button2.grid(column=1, row=30)

button3 = ttk.Button(frame, text="Exit", command=click_button3)
button3.grid(column=2, row=30)

for child in frame.winfo_children():
    child.grid_configure(padx=10, pady=10)

root.mainloop()
