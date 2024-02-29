import tkinter as tk
from math import sqrt, sin, cos, tan, radians

def on_click(button_value):
    current_text = entry_var.get()

    if button_value == '=':
        try:
            result = eval(current_text)
            entry_var.set(result)
        except:
            entry_var.set("Error")
    elif button_value == 'C':
        entry_var.set('')
    elif button_value == 'sqrt':
        try:
            result = sqrt(float(current_text))
            entry_var.set(result)
        except:
            entry_var.set("Error")
    elif button_value == 'sin':
        try:
            result = sin(radians(float(current_text)))
            entry_var.set(result)
        except:
            entry_var.set("Error")
    elif button_value == 'cos':
        try:
            result = cos(radians(float(current_text)))
            entry_var.set(result)
        except:
            entry_var.set("Error")
    elif button_value == 'tan':
        try:
            result = tan(radians(float(current_text)))
            entry_var.set(result)
        except:
            entry_var.set("Error")
    else:
        entry_var.set(current_text + button_value)

def generate_buttons(root, buttons, rows, columns):
    for button_text, row_val, col_val in buttons:
        tk.Button(root, text=button_text, padx=20, pady=20, font=('Arial', 14),
                  command=lambda b=button_text: on_click(b)).grid(row=row_val, column=col_val)

# Create the main window
root = tk.Tk()
root.title("Dynamic Calculator")

# Entry widget for display
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, justify='right', font=('Arial', 14))
entry.grid(row=0, column=0, columnspan=6)

# Define buttons properties
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0), ('sqrt', 5, 1), ('sin', 5, 2), ('cos', 5, 3), ('tan', 5, 4)
]

# Number of rows and columns for the grid
num_rows = 6
num_columns = 5

# Generate buttons dynamically
generate_buttons(root, buttons, num_rows, num_columns)

# Run the GUI
root.mainloop()
