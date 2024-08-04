#Imports necessary libraries for Tkinter GUI
import tkinter
from tkinter import *

#Defines the program as the variable "root"
root=Tk()
#Defines the title of the program
root.title("Type in Morse Code!")
#Changes the icon of the program to the desired icon
root.iconbitmap("C:/Users/hp/Downloads/morsecode.ico")
#Changes the background to peach puff
root.config(background="peachpuff")
#Changes the dimensions
root.geometry("1040x550")

#Defines the label which is supposed to say "Type in Arabic")
TypeinMorseCode=Label(root, text="Type in Morse Code!")
#Font adjustments
TypeinMorseCode.config(font=("Helvetica", 27, "bold"), bg="peachpuff", fg="white")
#Loads the label and sets its position
TypeinMorseCode.grid(row=0, columnspan=13, rowspan=1)

#Adds empty textbook, define properties, disables text widget so text can not be inputted the user
my_text=Text(root,width=80,state="disabled",font=("Helvetica", 16, "bold"), bg="white", height=4)
#Sets padding and position
my_text.grid(padx=10,pady=20,row=1, columnspan=13)

#Functions for buttons
def a_click():
    #Makes the state of the text widget normal for the time being so text can be inserted
    my_text.config(state="normal")
    #Appends "a" to the end of the text in the text widget
    my_text.insert(tkinter.END, ".- ")
    #Redisables the text widget so the user can not input text
    my_text.config(state="disabled")

def b_click():
    my_text.config(state="normal")
    my_text.insert(tkinter.END, "-... ")
    my_text.config(state="disabled")

def c_click():
    my_text.config(state="normal")
    my_text.insert(tkinter.END, "-.-. ")
    my_text.config(state="disabled")

def d_click():
    my_text.config(state="normal")
    my_text.insert(tkinter.END, "-.. ")
    my_text.config(state="disabled")

def e_click():
    my_text.config(state="normal")
    my_text.insert(tkinter.END, ". ")
    my_text.config(state="disabled")

def f_click():
    my_text.config(state="normal")
    my_text.insert(tkinter.END, "..-. ")
    my_text.config(state="disabled")

def g_click():
    my_text.config(state="normal")
    my_text.insert(tkinter.END, "--. ")
    my_text.config(state="disabled")

def h_click():
    my_text.config(state="normal")
    my_text.insert(tkinter.END, ".... ")
    my_text.config(state="disabled")

def i_click():
    my_text.config(state="normal")
    my_text.insert(tkinter.END, ".. ")
    my_text.config(state="disabled")

def j_click():
    my_text.config(state="normal")
    my_text.insert(tkinter.END, ".--- ")
    my_text.config(state="disabled")

def k_click():
    my_text.config(state="normal")
    my_text.insert(tkinter.END, "-.- ")
    my_text.config(state="disabled")

def l_click():
    my_text.config(state="normal")
    my_text.insert(tkinter.END, ".-.. ")
    my_text.config(state="disabled")

def m_click():
    my_text.config(state="normal")
    my_text.insert(tkinter.END, "-- ")
    my_text.config(state="disabled")

def n_click():
    my_text.config(state="normal")
    my_text.insert(tkinter.END, "-. ")
    my_text.config(state="disabled")

def o_click():
    my_text.config(state="normal")
    my_text.insert(tkinter.END, "--- ")
    my_text.config(state="disabled")

def p_click():
    my_text.config(state="normal")
    my_text.insert(tkinter.END, ".--. ")
    my_text.config(state="disabled")

def q_click():
    my_text.config(state="normal")
    my_text.insert(tkinter.END, "--.- ")
    my_text.config(state="disabled")

def r_click():
    my_text.config(state="normal")
    my_text.insert(tkinter.END, ".-. ")
    my_text.config(state="disabled")

def s_click():
    my_text.config(state="normal")
    my_text.insert(tkinter.END, "... ")
    my_text.config(state="disabled")

def t_click():
    my_text.config(state="normal")
    my_text.insert(tkinter.END, "- ")
    my_text.config(state="disabled")

def u_click():
    my_text.config(state="normal")
    my_text.insert(tkinter.END, "..- ")
    my_text.config(state="disabled")

def v_click():
    my_text.config(state="normal")
    my_text.insert(tkinter.END, "...- ")
    my_text.config(state="disabled")

def w_click():
    my_text.config(state="normal")
    my_text.insert(tkinter.END, ".-- ")
    my_text.config(state="disabled")

def x_click():
    my_text.config(state="normal")
    my_text.insert(tkinter.END, "-..- ")
    my_text.config(state="disabled")

def y_click():
    my_text.config(state="normal")
    my_text.insert(tkinter.END, "-.-- ")
    my_text.config(state="disabled")

def z_click():
    my_text.config(state="normal")
    my_text.insert(tkinter.END, "--.. ")
    my_text.config(state="disabled")

def space():
    my_text.config(state="normal")
    my_text.insert(tkinter.END, "/ ")
    my_text.config(state="disabled")
def clear():
    #Makes the state of the text widget normal so text can be inserted
    my_text.config(state="normal")
    #Deletes all the text in the text widget
    my_text.delete("1.0","end")
    #Redisables the text widget so text can not be inputted by the user
    my_text.config(state="disabled")
def copy():
    #Clears the clipboard so what is copied is not joined with the last copied thing in the clipboard
    root.clipboard_clear()
    #Copies the text of the text widget to the clipboard
    root.clipboard_append(my_text.get('1.0', tkinter.END))

#Create all alphabetical buttons as well as clear, space and copy
a=Button(root,text="a", font=72, padx=40, pady=30, bg="white", command=a_click)
b=Button(root,text="b", font=72, padx=40, pady=30, bg="white", command=b_click)
c=Button(root,text="c", font=72, padx=40, pady=30, bg="white", command=c_click)
d=Button(root,text="d", font=72, padx=40, pady=30, bg="white", command=d_click)
e=Button(root,text="e", font=72, padx=40, pady=30, bg="white", command=e_click)
f=Button(root,text="f", font=72, padx=40, pady=30, bg="white", command=f_click)
g=Button(root,text="g", font=72, padx=40, pady=30, bg="white", command=g_click)
h=Button(root,text="h", font=72, padx=40, pady=30, bg="white", command=h_click)
i=Button(root,text="i", font=72, padx=45, pady=30, bg="white", command=i_click)
j=Button(root,text="j", font=72, padx=50, pady=30, bg="white", command=j_click)
k=Button(root,text="k", font=72, padx=45, pady=30, bg="white", command=k_click)
l=Button(root,text="l", font=72, padx=45, pady=30, bg="white", command=l_click)
m=Button(root,text="m", font=72, padx=45, pady=30, bg="white", command=m_click)
n=Button(root,text="n", font=72, padx=40, pady=30, bg="white", command=n_click)
o=Button(root,text="o", font=72, padx=40, pady=30, bg="white", command=o_click)
p=Button(root,text="p", font=72, padx=45, pady=30, bg="white", command=p_click)
q=Button(root,text="q", font=72, padx=40, pady=30, bg="white", command=q_click)
r=Button(root,text="r", font=72, padx=40, pady=30, bg="white", command=r_click)
s=Button(root,text="s", font=72, padx=40, pady=30, bg="white", command=s_click)
t=Button(root,text="t", font=72, padx=40, pady=30, bg="white", command=t_click)
u=Button(root,text="u", font=72, padx=47, pady=30, bg="white", command=u_click)
v=Button(root,text="v", font=72, padx=40, pady=30, bg="white", command=v_click)
x=Button(root,text="x", font=72, padx=40, pady=30, bg="white", command=w_click)
w=Button(root,text="w", font=72, padx=40, pady=30, bg="white", command=x_click)
y=Button(root,text="y", font=72, padx=40, pady=30, bg="white", command=y_click)
z=Button(root,text="z", font=72, padx=40, pady=30, bg="white", command=z_click)
spacebutton=Button(root,text="SPACE", font=72, padx=125, pady=30, bg="turquoise2", command=space)
clear=Button(root,text="CLEAR", font=72, padx=20, pady=30, bg="sienna1", fg="white", command=clear)
copy=Button(root,text="COPY!", font=72, padx=80, pady=30, bg="gold", fg="black", command=copy)

#Position
q.grid(row=2,column=0)
w.grid(row=2,column=1)
e.grid(row=2,column=2)
r.grid(row=2,column=3)
t.grid(row=2,column=4)
y.grid(row=2,column=5)
u.grid(row=2,column=6)
i.grid(row=2,column=7)
o.grid(row=2,column=8)
p.grid(row=2,column=9)
a.grid(row=3, column=0)
s.grid(row=3, column=1)
d.grid(row=3, column=2)
f.grid(row=3, column=3)
g.grid(row=3, column=4)
h.grid(row=3, column=5)
j.grid(row=3, column=6)
k.grid(row=3, column=7)
l.grid(row=3, column=8)
clear.grid(row=3, column=9)
z.grid(row=4, column=0)
x.grid(row=4, column=1)
c.grid(row=4, column=2)
v.grid(row=4, column=3)
b.grid(row=4, column=4)
n.grid(row=4, column=5)
m.grid(row=4, column=6)
spacebutton.grid(row=4, column=7, columnspan=3)
copy.grid(row=5, columnspan=13)

#Loads the whole program
root.mainloop()