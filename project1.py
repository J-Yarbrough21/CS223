#!/usr/bin/env python3
from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("980x450")
window.title("Pay Check Lab")

label = Label(
    window,
    text="First Name",
    font=("Times", 12, "bold"),
    fg="#030303",
    justify=("left"),
)
label.place(x=3, y=20, width=150, height=30)

label = Label(
    window, text="Last Name", font=("Times", 12, "bold"), fg="#030303", justify=("left")
)
label.place(x=190, y=20, width=150, height=30)

label = Label(
    window,
    text="Rate of Pay",
    font=("Times", 12, "bold"),
    fg="#030303",
    justify=("left"),
)
label.place(x=380, y=20, width=150, height=30)

label = Label(
    window,
    text="Hours Worked",
    font=("Times", 12, "bold"),
    fg="#030303",
    justify=("left"),
)
label.place(x=580, y=20, width=150, height=30)

label = Label(
    window,
    text="Overtime Hours ",
    font=("Times", 12, "bold"),
    fg="#030303",
    justify=("left"),
)
label.place(x=775, y=20, width=150, height=30)

label = Label(
    window,
    text="Employee Full Name :",
    font=("Times", 12, "bold"),
    fg="#030303",
    justify=("left"),
)
label.place(x=13, y=150, width=200, height=30)

label = Label(
    window,
    text="Employee Hourly Wage : $",
    font=("Times", 12, "bold"),
    fg="#030303",
    justify=("left"),
)
label.place(x=3, y=200, width=200, height=30)

label = Label(
    window,
    text="Total Hours Worked :",
    font=("Times", 12, "bold"),
    fg="#030303",
    justify=("left"),
)
label.place(x=13, y=250, width=200, height=30)

label = Label(
    window,
    text="Regular Pay = $",
    font=("Times", 12, "bold"),
    fg="#030303",
    justify=("left"),
)
label.place(x=388, y=150, width=150, height=30)

label = Label(
    window,
    text="Overtime Pay = $",
    font=("Times", 12, "bold"),
    fg="#030303",
    justify=("left"),
)
label.place(x=383, y=200, width=150, height=30)

label = Label(
    window,
    text="Gross Pay = $",
    font=("Times", 12, "bold"),
    fg="#030303",
    justify=("left"),
)
label.place(x=393, y=250, width=150, height=30)

label = Label(
    window,
    text="Net Pay = $",
    font=("Times", 12, "bold"),
    fg="#030303",
    justify=("left"),
)
label.place(x=400, y=300, width=150, height=30)

label = Label(
    window, text="FITW = $", font=("Times", 12, "bold"), fg="#030303", justify=("left")
)
label.place(x=713, y=150, width=150, height=30)

label = Label(
    window,
    text="Medicare = $",
    font=("Times", 12, "bold"),
    fg="#030303",
    justify=("left"),
)
label.place(x=700, y=200, width=150, height=30)

label = Label(
    window, text="OASDI = $", font=("Times", 12, "bold"), fg="#030303", justify=("left")
)
label.place(x=709, y=250, width=150, height=30)

label = Label(
    window,
    text="Total Tax = $",
    font=("Times", 12, "bold"),
    fg="#030303",
    justify=("left"),
)
label.place(x=701, y=300, width=150, height=30)

first_name = StringVar()
last_name = StringVar()
payratep = StringVar()
hoursworkedn = StringVar()
overtimeb = StringVar()
gross_pay = StringVar()
net_pay = StringVar()
fitw = StringVar()
med_c = StringVar()
oasdi = StringVar()
ttax = StringVar()

FN_entry = Entry(window, textvariable=first_name, font=("Times", 12))
FN_entry.place(x=35, y=55, width=150, height=30)

LN_entry = Entry(window, textvariable=last_name, font=("Times", 12))
LN_entry.place(x=225, y=55, width=150, height=30)

RP_entry = Entry(window, textvariable=payratep, font=("Times", 12))
RP_entry.place(x=415, y=55, width=150, height=30)

HW_entry = Entry(window, textvariable=hoursworkedn, font=("Times", 12))
HW_entry.place(x=605, y=55, width=150, height=30)

OT_entry = Entry(window, textvariable=overtimeb, font=("Times", 12))
OT_entry.place(x=795, y=55, width=150, height=30)

m_1_str = StringVar()
m_2_str = StringVar()
m_3_str = StringVar()
m_4_str = StringVar()
m_5_str = StringVar()
m_6_str = StringVar()
m_7_str = StringVar()
m_8_str = StringVar()
m_9_str = StringVar()
m_10_str = StringVar()
m_11_str = StringVar()

m_1 = Label(
    window,
    text="",
    textvariable=m_1_str,
    font=("Times", 12, "bold"),
    justify=("left"),
    fg="#030303",
).place(x=200, y=153)
m_2 = Label(
    window,
    text="",
    textvariable=m_2_str,
    font=("Times", 12, "bold"),
    justify=("left"),
    fg="#030303",
).place(x=200, y=202)
m_3 = Label(
    window,
    text="",
    textvariable=m_3_str,
    font=("Times", 12, "bold"),
    justify=("left"),
    fg="#030303",
).place(x=200, y=252)
m_4 = Label(
    window,
    text="",
    textvariable=m_4_str,
    font=("Times", 12, "bold"),
    justify=("left"),
    fg="#030303",
).place(x=525, y=153)
m_5 = Label(
    window,
    text="",
    textvariable=m_5_str,
    font=("Times", 12, "bold"),
    justify=("left"),
    fg="#030303",
).place(x=525, y=202)
m_6 = Label(
    window,
    text="",
    textvariable=m_6_str,
    font=("Times", 12, "bold"),
    justify=("left"),
    fg="#030303",
).place(x=525, y=252)
m_7 = Label(
    window,
    text="",
    textvariable=m_7_str,
    font=("Times", 12, "bold"),
    justify=("left"),
    fg="#030303",
).place(x=835, y=153)
m_8 = Label(
    window,
    text="",
    textvariable=m_8_str,
    font=("Times", 12, "bold"),
    justify=("left"),
    fg="#030303",
).place(x=835, y=202)
m_9 = Label(
    window,
    text="",
    textvariable=m_9_str,
    font=("Times", 12, "bold"),
    justify=("left"),
    fg="#030303",
).place(x=835, y=252)
m_10 = Label(
    window,
    text="",
    textvariable=m_10_str,
    font=("Times", 12, "bold"),
    justify=("left"),
    fg="#030303",
).place(x=835, y=302)
m_11 = Label(
    window,
    text="",
    textvariable=m_11_str,
    font=("Times", 12, "bold"),
    justify=("left"),
    fg="#030303",
).place(x=525, y=302)


def calculate():
    f_name = str(first_name.get())
    l_name = str(last_name.get())

    payrate = float(payratep.get())
    hours = float(hoursworkedn.get())
    overtimehours = float(overtimeb.get())

    full_name = f_name + " " + l_name
    reg_total_pay = payrate * hours
    tot_hours = hours + overtimehours
    ot_pay = (payrate * 1.50) * overtimehours
    total_pay = reg_total_pay + ot_pay
    fed_with = total_pay * 0.12
    med_care = total_pay * 0.014
    oas_di = total_pay * 0.06
    tot_tax = fed_with + med_care + oas_di
    net_pay = total_pay - tot_tax

    m_1_str.set(full_name)
    m_2_str.set("{:.2f}".format(payrate))
    m_3_str.set("{:.2f}".format(tot_hours))
    m_4_str.set("{:.2f}".format(reg_total_pay))
    m_5_str.set("{:.2f}".format(ot_pay))
    m_6_str.set("{:.2f}".format(total_pay))
    m_7_str.set("{:.2f}".format(fed_with))
    m_8_str.set("{:.2f}".format(med_care))
    m_9_str.set("{:.2f}".format(oas_di))
    m_10_str.set("{:.2f}".format(tot_tax))
    m_11_str.set("{:.2f}".format(net_pay))


button = Button(window, text="Calculate", command=calculate, font=("Times", 12, "bold"))
button.place(x=133, y=375, width=150, height=30)


def clear():
    FN_entry.delete(0, END)
    LN_entry.delete(0, END)
    RP_entry.delete(0, END)
    HW_entry.delete(0, END)
    OT_entry.delete(0, END)
    m_1_str.set("")
    m_2_str.set("")
    m_3_str.set("")
    m_4_str.set("")
    m_5_str.set("")
    m_6_str.set("")
    m_7_str.set("")
    m_8_str.set("")
    m_9_str.set("")
    m_10_str.set("")
    m_11_str.set("")


button = Button(window, text="Clear", command=clear, font=("Times", 12, "bold"))
button.place(x=415, y=375, width=150, height=30)


def destroy():
    window.destroy()


button = Button(window, text="Exit", command=destroy, font=("Times", 12, "bold"))
button.place(x=698, y=375, width=150, height=30)

window.mainloop()
