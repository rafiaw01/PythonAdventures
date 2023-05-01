from tkinter import *

from GraphicsDemo import window


class MultipleSelection:
    def __init__(self):
        window = Tk()
        window.title("Multiple Selection")

        frame1 = Frame(window)
        frame1.pack()
        self.v1= IntVar()
        cbtBold = Checkbutton(frame1, text = "Bold", variable = self.v1, command = self.processCheckbutton)
        self.v2 = IntVar()
        rbRed = Radiobutton(frame1, text = "Red", bg = "red",variable = self.v2, value = 1,command = self.processRadiobutton)
        rbYellow = Radiobutton(frame1, text = "Yellow",
    bg = " yellow", variable = self.v2, value = 2,
    command = self.processRadiobutton)
        cbtBold.grid(row = 1, column = 1)
        rbRed.grid(row = 1, column = 2)
        rbYellow.grid(row = 1, column = 3)


       frame2 = Frame(window)
       frame2.pack()
       label= Label(frame2, text =" Enter your name:")
       self.name = StringVar()
       entryName = Entry(frame2,textvariable = self.name)
       btGetName = Button(frame2, text = "Get Name",command = self.processButton)
       message=Message(frame2, text = "It is a widgets demo")
       label.grid(row=1, column=1)
       entryName.grid(row=1,column=2)
       btGetName.grid(row=1,column=3)
       message.grid(row=1, column=4)

          Text=Text(window)
          Text.pack()
          Text.insert(END,
          "Tip\nThe best way to lean Tkinter is to read")
          Text.insert(END,
          "these carefully designed examples and use them")
          Text.insert(END,"to create your applications.")

          window.mainloop()
          def processCheckbutton(self):
          print("check button is" + ("checked" if Self.v1.get() == 1 else "unchecked"))

    def processRadiobutton(self):
        print(("Red" if self.v2.get() == 1 else "Yellow")
              + " is selected")
        def processButton(Self):
            print("Your name is "+ self.name.get())

        MultipleSelection()


