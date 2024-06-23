from tkinter import *

def press(button):  # func press - argument button
    current_expression = equation.get()  # gets current value from text field
    if button == 'C':  # if C is pressed, clears text field
        equation.set('')
    elif button == '=':  # evaluates the expression and displays results
        try:
            result = str(eval(current_expression))
            equation.set(result)
        except Exception as e:
            equation.set("Error")
    else:
        equation.set(current_expression + button)

# initializes GUI application
gui = Tk()
# window title and size
gui.title("CodSoft Calculator")
gui.geometry("400x600")  # Corrected geometry specifier

# created StringVar object to hold a string value
equation = StringVar()

expression_field = Entry(gui, textvariable=equation, font=('Arial', 18), bd=5, justify=RIGHT)
expression_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

#define layout and contents of button
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (text, row, col) in buttons:
    button = Button(gui, text=text, font=('Arial', 14), width=5, height=2, command=lambda t=text: press(t))
    button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

# configure row and column weights to make buttons expandable, ensuring the buttons and entry widget resize properly with the window.
for i in range(5):
    gui.grid_rowconfigure(i, weight=1)
for i in range(4):
    gui.grid_columnconfigure(i, weight=1)

gui.mainloop()
