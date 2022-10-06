from tkinter import *
Window=Tk()

Window.title('SimpleInterest Clculator')
Window.geometry("400x400")
Window.configure(bg='lightcyan')

def calculate_SI():
    p = float(Principle.get())
    r = float(ROI.get())
    t = float(T.get())
    i = (p*r*t)/100
   
    SI=round(i, 2)

    a = (p+SI)
    
    A = round(a)
    
    name = username.get()

    result_label.destroy()

    msg=""

    output_message=Label(result_frame,text="Interest on Rs." + str(p) + " at rate of Interest " + str(r) + " %  for " + str(t) + " yrs is " + str(SI) + " and Hence,the Amount need to be returned is " + str(A) ,bg = "lightcyan", font=("Calibri", 12), width=100)
    output_message.place(x=20,y=40)
    output_message.pack()

app_label=Label(Window, text="SI CALCULATOR", fg = "black", bg = "lightcyan", font=("Calibri", 20),bd=5)
app_label.place(x=100, y=20)

name_label=Label(Window, text="Your Name", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=1)
name_label.place(x=20, y=90)
username=Entry(Window, text="", bd=2, width=22)
username.place(x=150, y=92)

Principle_label=Label(Window, text="Principal", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=1)
Principle_label.place(x=20, y=90)
Principle=Entry(Window, text="", bd=2, width=22)
Principle.place(x=150, y=92)

ROI_label=Label(Window, text="Rate of Interest", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=1)
ROI_label.place(x=20, y=140)
ROI=Entry(Window, text="", bd=2, width=22)
ROI.place(x=150, y=142)

T_label=Label(Window, text="Time", fg="black", bg="lightcyan", font=("Calibri", 12),bd=1)
T_label.place(x=20, y=185)
T=Entry(Window, text="", bd=2, width=22)
T.place(x=150, y=187)

calculate_button=Button(Window,text="CALCULATE",fg = "black", bg = "cyan",bd=4,command=calculate_SI)
calculate_button.place(x=20,y=250)

result_frame = LabelFrame(Window,text="Result", bg = "lightcyan", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=300)

result_label=Label(result_frame,text=" ", bg = "lightcyan", font=("Calibri", 12), width=100)
result_label.place(x=20,y=20)
result_label.pack()



Window.mainloop()