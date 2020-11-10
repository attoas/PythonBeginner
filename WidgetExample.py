from tkinter import *

def sayHelloWorld():
   print("Hello World")

MainWindow1 = Tk()
button = Button(MainWindow1,text = "Click me",command = sayHelloWorld)
button.place(x = 50, y = 20)
MainWindow1.mainloop()

MainWindow2 = Tk()
button = Button(MainWindow2,text = "Click me 2",command = sayHelloWorld)
button.place(x = 50, y = 20)
MainWindow2.mainloop()