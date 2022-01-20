#!/usr/bin/env python3
import tkinter as tk
import tkinter.font as tkFont

# setting up the window
root = tk.Tk()
width = 900
height = 900
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
root.title("Average Test Scores-Lab2")
ft = tkFont.Font(family="Times", size=12, weight="bold")
line_height = ft.metrics("linespace")
alignstr = "%dx%d+%d+%d" % (
    width,
    height,
    (screenwidth - width) / 2,
    (screenheight - height) / 2,
)
root.geometry(alignstr)
root.resizable(width=False, height=False)

# frame = tk.Frame(root, width=10, height=10, padding="10 10 10 10")
# frame.pack(fill=tk.BOTH, expand=True)


def label_settings(
    label_handle, ft, line_height, label_text="dummy", lx=0, ly=0, lw=30
):
    label_handle["activebackground"] = "white"
    label_handle["activeforeground"] = "white"
    label_handle["bg"] = "white"
    label_handle["disabledforeground"] = "#ffffff"
    label_handle["font"] = ft
    label_handle["fg"] = "black"
    label_handle["justify"] = "left"
    label_handle["text"] = label_text
    label_handle.place(x=lx, y=ly, width=lw, height=line_height)


def entry_box_settings(entry_handle, ft, line_height, ex, ey, ew):
    entry_handle["bg"] = "white"
    entry_handle["borderwidth"] = "1px"
    entry_handle["font"] = ft
    entry_handle["fg"] = "black"
    entry_handle["justify"] = "left"
    entry_handle["text"] = ""
    entry_handle["relief"] = "sunken"
    entry_handle.place(x=ex, y=ey, width=ew, height=line_height + 10)


first_nameLabel = tk.Label(root)
width = ft.measure("Student First Name: ")
label_settings(
    first_nameLabel,
    ft,
    line_height,
    label_text="Student First Name: ",
    lx=10,
    ly=10,
    lw=width,
)

first_nameEntry = tk.Entry(root)
width = ft.measure("A" * 32)
entry_box_settings(
    first_nameEntry,
    ft,
    line_height,
    ex=ft.measure("Student First Name: ") + 10,
    ey=5,
    ew=width,
)
first_nameStr = tk.StringVar()
first_nameEntry["textvariable"] = first_nameStr

last_nameLabel = tk.Label(root)
width = ft.measure("Student First Name: ")
label_settings(
    last_nameLabel,
    ft,
    line_height,
    label_text="Student Last Name: ",
    lx=10,
    ly=45,
    lw=width,
)

last_nameEntry = tk.Entry(root)
width = ft.measure("A" * 32)
entry_box_settings(
    last_nameEntry,
    ft,
    line_height,
    ex=ft.measure("Student First Name: ") + 10,
    ey=40,
    ew=width,
)
last_nameStr = tk.StringVar()
last_nameEntry["textvariable"] = last_nameStr


# score_oneLabel = ttk.Label(frame, text="Score 1: ").grid(column=0, row=4, sticky=tk.W)
# score_oneText = tk.StringVar()
# score_oneEntry = ttk.Entry(frame, width=200, textvariable=score_oneText).grid(
#     column=2, row=4
# )

# score_twoLabel = ttk.Label(frame, text="Score 2: ").grid(column=0, row=6, sticky=tk.W)
# score_twoText = tk.StringVar()
# score_twoEntry = ttk.Entry(frame, width=200, textvariable=score_twoText).grid(
#     column=2, row=6
# )

# score_threeLabel = ttk.Label(frame, text="Score 3: ").grid(column=0, row=8, sticky=tk.W)
# score_threeText = tk.StringVar()
# score_threeEntry = ttk.Entry(frame, width=200, textvariable=score_threeText).grid(
#     column=2, row=8
# )

# fn_Text_str = tk.StringVar()
# fn_Label = ttk.Label(frame, textvariable=fn_Text_str, width=200).grid(
#     column=0, row=10, sticky=tk.W
# )
# fn_Entry = ttk.Entry(frame, width=200).grid(column=2, row=10)
# fn_Text_str.set("")

# av_Text_str = tk.StringVar()
# av_Label = ttk.Label(frame, textvariable=av_Text_str, width=200).grid(
#     column=0, row=14, sticky=tk.W
# )
# av_Entry = ttk.Entry(frame, width=200).grid(column=2, row=14)
# av_Text_str.set("")

# ts_Text_str = tk.StringVar()
# ts_Label = ttk.Label(frame, textvariable=ts_Text_str, width=200).grid(
#     column=0, row=16, sticky=tk.W
# )
# ts_Entry = ttk.Entry(frame, width=200).grid(column=2, row=16)
# ts_Text_str.set("")


# def click_button1():
#     fullname = str(first_nameText.get()) + str(last_nameText.get())
#     fn_Text_str.set = fullname


# def click_button2():
#     root.title("this is the result of button 2")


# def click_button3():
#     root.destroy()


# button1 = ttk.Button(frame, text="Score", command=click_button1)
# button1.grid(column=0, row=10)

# button2 = ttk.Button(frame, text="Clear", command=click_button2)
# button2.grid(column=1, row=10)

# button3 = ttk.Button(frame, text="Exit", command=click_button3)
# button2.grid(column=2, row=10)

# for child in frame.winfo_children():
#     child.grid_configure(padx=10, pady=10)

root.mainloop()
