from tkinter import *
from tkinter import messagebox
import time
import pyautogui

main = Tk()
main.title("AutoTyper")
main.configure(width=1000,bg="lightblue")

#------------------------Size configuration-----------------------#
# main.maxsize(1000,600)
main.minsize(1000,600)
posRight = int(main.winfo_screenwidth()/10)#to center window
posDown = int(main.winfo_screenheight()/10)#to center window
main.geometry("+{}+{}".format(posRight, posDown))


#------------------Functions and Variable Used---------------------#
Timer = IntVar()

def Start():
    messagebox.showinfo("Process","After pressing enter, your execution start within {0}".format(Timer.get()))
    time.sleep(Timer.get())
    pyautogui.write(InputData.get(1.0, "end-1c"))

#Main Window Frames decleartion
DataFrame = Frame(main)
DataFrame.place(x=0,y=0,relheight=1,relwidth=0.7)

SettingFrame = Frame(main,bg="#358")
SettingFrame.place(relx=0.7,y=0,relheight=1,relwidth=0.3)


#DataFrame element
InputData = Text(DataFrame,font="Arial 15",height=1000,width=360,wrap=NONE)
InputData.pack()

#Setting Frame element

Label(SettingFrame,text="Set-Timer:",font="Arial 20",bg="#358",fg="white").place(relx=0.12,rely=0.25,relwidth=0.5)

OptionMenu(SettingFrame, Timer, 0,3,5,10,20).place(relx=0.6, rely=0.26, relwidth=0.2)

Button(SettingFrame,text="Start",command=Start,font="Arial 20",activebackground="#247",activeforeground="white").place(relx=0.2,rely=0.7,relwidth=0.6,relheight=0.1)


main.mainloop()