import tkinter as tk
from tkinter import *
import random

title = str(input("Enter the title: "))

window = tk.Tk()
window.geometry("1080x980")
window.title(title)


text = StringVar()
digit = IntVar()

final_digit = IntVar()
guess = IntVar()

num = random.randint(1,10)

text.set("# between 1-10")
digit.set(5)
final_digit.set(digit.get())


def function():
    x = guess.get()
    final_digit.set(digit.get())
    if digit.get() > 0:

        if x > 10 or x < 0:
            text.set("You just lost 1 Chance")
            digit.set(digit.get()-1)
            final_digit.set(digit.get())
    
        elif num == x:
            text.set("Congratulation YOU WON!!!")
            digit.set(digit.get()-1) # Your attempts decreases
            final_digit.set(digit.get())

        elif num > x:
            text.set("Your guess was too low: Guess a number higher ")
            digit.set(digit.get()-1)
            final_digit.set(digit.get())

        elif num < x:
            text.set("Your guess was too High: Guess a number Lower ")
            digit.set(digit.get()-1)
            final_digit.set(digit.get())
    else:
        text.set("Game Over You Lost")

def function_2():
    Label(window, text='LOL', font=("Courier", 25)).place(relx=0.5, rely=0.045, anchor=CENTER)
    Label(window, text='Do u want to exit?', font=("Courier", 25)).place(relx=0.5, rely=0.01, anchor=CENTER)

    Button(window, width=5, text='Exit', font=('UBUNTU', 11), command=function_3, relief=GROOVE, bg='green').place(relx=0.8, rely=0.2, anchor=CENTER)

def function_3():
    window.destroy()


#* Entries
Entry(window, textvariable=guess, width=3, font=('Ubuntu', 50), relief=GROOVE).place(relx=0.5, rely=0.3, anchor=CENTER)

Entry(window, textvariable=text, width=50, font=('Courier', 15), relief=GROOVE, bg='orange').place(relx=0.5, rely=0.7, anchor=CENTER)

Entry(window, textvariable=final_digit, width=2, font=('Ubuntu', 24), relief=GROOVE).place(relx=0.61, rely=0.85, anchor=CENTER)


#? Labels
Label(window, text='I challenge you to guess the number ', font=("Courier", 25)).place(relx=0.5, rely=0.09, anchor=CENTER)

Label(window, text='Score out of 5', font=("Courier", 25)).place(relx=0.3, rely=0.85, anchor=CENTER)


#! Buttons
Button(window, width=8, text='Guess IT!', font=('UBUNTU', 11), command=function, relief=GROOVE, bg='green').place(relx=0.8, rely=0.3, anchor=CENTER)

Button(window, width=5, text='Say Hi', font=('UBUNTU', 11), command=function_2, relief=GROOVE, bg='green').place(relx=0.8, rely=0.4, anchor=CENTER)

#* Mainloop
window.mainloop()