import __main__
from tkinter import *
from tkinter import ttk


#! Function:

def motion_detection():
    print('Motion Detection activated!')

def audio_lure():
    print('Audio Lure has been set')

def silent_ventilation():
    print('Silent Ventilation is active')
    window.deiconify()

def quit():
    print('You have quit!')
    window.withdraw()

def action():
    pass

def submit():

    search_result = entry.get()

    if(search_result == "MONETZ"):
        print("You did right!")
    else:
        print("Not that one! Try again.")

#! Application:

#? Window
window = Tk()

window.geometry('420x420')
window.title("V.I.S.E. Application")
icon = PhotoImage(file='Python/Projects/gui/logo.png')
window.iconphoto(True,icon)
#window.config(background="#5cfcff") # HEX color also supportive


#? Internal variables
int_x = IntVar()
int_y = IntVar()


#? Menubar
menubar = Menu(window)
window.config(menu=menubar)

#* File Menu
fileMenu = Menu(menubar, tearoff=0, font=("Consolas", 15))
menubar.add_cascade(label="Menu", menu=fileMenu)
fileMenu.add_command(label="Motion Detection", command=motion_detection, compound='left')
fileMenu.add_command(label="Audio Lure", command=audio_lure, compound='left')
fileMenu.add_command(label="Silent Ventilation", command=silent_ventilation, compound='left')
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=quit, compound='left' )

#* Edit Menu
edit_menu = Menu(menubar, tearoff=0, font=("Consolas", 15))
menubar.add_cascade(label="Extra", menu=edit_menu)
edit_menu.add_command(label="Camera", compound='left')
edit_menu.add_command(label="Mic", compound='left')
edit_menu.add_command(label="Mute", compound='left')

#* Social Media Menu
# sm = social media
sm_menu = Menu(menubar, tearoff=0, font=("Consolas", 15))
menubar.add_cascade(label="Social Media", menu=sm_menu)
sm_menu.add_command(label="Telegram", compound='left')
sm_menu.add_command(label="X", compound='left')
sm_menu.add_command(label="LinkedIn", compound='left')


#? Notebook
notebook = ttk.Notebook(window)

tab1 = Frame(notebook) # new frame for tab 1
tab2 = Frame(notebook) # new frame for tab 2
tab3 = Frame(notebook) # new frame for tab 3

#? Entry
entry = Entry()
entry.pack()

submit = Button(window, text="Submit", command=submit)
submit.pack()





notebook.add(tab1, text="Motion Detection")
notebook.add(tab2, text="Audio Lure")
notebook.add(tab3, text="Silent Ventilation")
notebook.pack(expand=True, fill="both")

Label(tab1, text="Welcome to the 'Motion Detection' tool!", width=50, height=25).pack()
Label(tab2, text="Welcome to the 'Audio Lure' tool!", width=50, height=25).pack()
Label(tab3, text="Welcome to the 'Silent Ventilation' tool!", width=50, height=25).pack()


#? Button
action = Button(window, text='Action', command=action, font=("Consolas")).pack(side = RIGHT)
do = Button(window, text='Do', command=action, font=("Consolas")).pack(side = LEFT)





window.mainloop()

if __name__ == __main__:
    print('this is the script area')