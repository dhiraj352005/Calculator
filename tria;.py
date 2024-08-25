import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Define a global variable to store the expression
expression = ""

# Define functions to handle button clicks
def add_number(number):
    global expression
    expression += str(number)
    equation.set(expression)

def add_operation(operation):
    global expression
    expression += operation
    equation.set(expression)

def clear():
    global expression
    expression = ""
    equation.set(expression)

def equal():
    try:
        global expression
        result = eval(expression)
        expression = str(result)
        equation.set(expression)
    except ZeroDivisionError:
        equation.set("Error: Division by zero")
    except SyntaxError:
        equation.set("Error: Invalid expression")

# Create an entry widget to display the expression
equation = tk.StringVar()
entry = tk.Entry(window, textvariable=equation)
entry.grid(row=0, column=0, columnspan=4)

# Create buttons for numbers
number_buttons = []
for i in range(10):
    button = tk.Button(window, text=str(i), command=lambda n=i: add_number(n))
    number_buttons.append(button)

# Create buttons for operations
operation_buttons = []
for operation in ("+", "-", "*", "/"):
    button = tk.Button(window, text=operation, command=lambda op=operation: add_operation(op))
    operation_buttons.append(button)

# Create a button for clearing the expression
clear_button = tk.Button(window, text="C", command=clear)

# Create a button for evaluating the expression
equal_button = tk.Button(window, text="=", command=equal)

# Layout the buttons
for i in range(3):
    for j in range(3):
        number_buttons[i * 3 + j].grid(row=i + 1, column=j, pady=5, padx=5)

for i, operation_button in enumerate(operation_buttons):
    operation_button.grid(row=i + 4, column=3, pady=5, padx=5)

clear_button.grid(row=4, column=0, columnspan=3, pady=5, padx=5)
equal_button.grid(row=5, column=0, columnspan=4, pady=5, padx=5)

# Start the main event loop
window.mainloop()
