from tkinter import *
from tkinter import INSERT
from tkinter import messagebox

def TimeTable():
    txtDisplay.delete('1.0', END)
    for x in range(1,13):
        try:
            m = int(text_input.get())
        except ValueError:
            messagebox.showinfo("Error", "You must enrty integer")
            break
        txtDisplay.insert(END, (x), '\t', "x", '\t', (m), '\t', "=", '\t', (x*m))
        txtDisplay.insert(END, "\n\n")

Multiply = Tk()
Multiply.title("Multiplication Table")
Multiply.resizable(0, 0)
text_input = StringVar()

label = Label(Multiply,
              text="Multiplication Table",
              font=("arial", 30, "bold"),
              fg="black"
              ).grid(row=0, column=0)

textInput = Entry(Multiply,
                  textvariable=text_input,
                  bd=30,
                  font=("arial", 20, "bold"),
                  fg="black",
                  insertwidth=4,
                  bg="powder blue",
                  justify="center"
                  ).grid(row=1, column=0)

txtDisplay = Text(Multiply,
                 width=20,
                 height=12,
                 bg="powder blue",
                 bd=23,
                 font=("arial", 20, "bold"))

txtDisplay.grid(row=2, column=0)

btnTimeTable = Button(Multiply,
                      padx=16,
                      pady=16,
                      bd=8,
                      fg="black",
                      font=("arial", 23, "bold"),
                      text="Multiplication",
                      bg="powder blue",
                      command= TimeTable,
                      width=18
                      ).grid(row=3, column=0)

Multiply.mainloop()
