from tkinter import *


def leftClickButton(event):
    print("Left Click")


def rightClickButton(event):
    print("Right Click")

def doubleLeftClickButton(event):
    print("Double Left Click")

def doubleRightClickButton(event):
    print("Double Right Click")

main = Tk()
button = Button(main, text="My Button !!")
button.pack()
button.bind('<Button-1>', leftClickButton)
button.bind('<Button-3>', rightClickButton)
button.bind('<Double-1>', doubleLeftClickButton)
button.bind('<Double-3>', doubleRightClickButton)

# <Button-1 คือ ซ้าย Button-2 คือปุ่มกลาง Button-3 คือ ปุ่มขวามือ
main.mainloop()