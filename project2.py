#!/user/bin/env/python3
import tkinter as tk
from tkinter import ttk
from xml.dom import pulldom
 
root = tk.Tk()
root.geometry("900x400")
root.title("Average Test Scores-Lab2")
 
frame = ttk.Frame(root,padding="10 10 10 10")
frame.pack(fill=tk.BOTH, expand=True)
 
ttk.Label(frame, text="Student First Name").grid(column=0, row=0, sticky=tk.W)
fnameText = tk.StringVar()
fnameEntry = ttk.Entry(frame, width=25, textvariable=fnameText).grid(column=0,row=2)
 
ttk.Label(frame, text="Student Last Name").grid(column=1, row=0, sticky=tk.W)
lnameText = tk.StringVar()
lnameEntry = ttk.Entry(frame, width=25, textvariable=lnameText).grid(column=1,row=2)
 
ttk.Label(frame, text="Score 1").grid(column=0, row=4, sticky=tk.W)
score1Text = tk.StringVar()
score1Entry = ttk.Entry(frame, width=25, textvariable=score1Text).grid(column=1,row=4)
 
ttk.Label(frame, text="Score 2").grid(column=0, row=5, sticky=tk.W)
score2Text = tk.StringVar()
score2Entry = ttk.Entry(frame, width=25, textvariable=score2Text).grid(column=1,row=5)
 
ttk.Label(frame, text="Score 3").grid(column=0, row=6, sticky=tk.W)
score3Text = tk.StringVar()
score3Entry = ttk.Entry(frame, width=25, textvariable=score3Text).grid(column=1,row=6)
 
ttk.Label(frame, text="Student Full Name").grid(column=3, row=0, sticky=tk.W)
fullnameText = tk.StringVar()
fullnameEntry = ttk.Entry (frame, width=25, textvariable=fullnameText, state="readonly").grid(column=4,row=0)
 
ttk.Label(frame, text="Average Score").grid(column=3, row=2, sticky=tk.W)
averageText = tk.StringVar()
averageEntry = ttk.Entry (frame, width=25, textvariable=averageText, state="readonly").grid(column=4,row=2)
 
ttk.Label(frame, text="Total Score").grid(column=3, row=4, sticky=tk.W)
totalText = tk.StringVar()
totalEntry = ttk.Entry (frame, width=25, textvariable=totalText, state="readonly").grid(column=4,row=4)
 
for child in frame.winfo_children():
    child.grid_configure(padx=10, pady=10)
       
#def click_button1():
    #fullnameText = fnameText+lnameText
    #totalText = score1Entry+score2Entry+score3Entry
    #averageText = round(totalText/3)
    #display=total and average of scores.
 
def click_button2():
    root.destroy()
 
button1 = ttk.Button(frame, text="Calculate", style = 'button1', command=None)
button1.grid (column=4,row = 11)
 
button2 = ttk.Button(frame, text="Clear", style = 'button2', command=click_button2)
button2.grid(column=2, row =11)
   
root.mainloop()
git pull
git stage*
git commit -m 'initial-load'
git push 