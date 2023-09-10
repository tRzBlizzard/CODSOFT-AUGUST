import tkinter as tk

# Function to evaluate the expression and update the display
def calculate():
    expression = entry.get()
    try:
        result = str(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Entry field for input and display
entry = tk.Entry(root, width=20, font=('Helvetica', 20), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Buttons for digits and operators
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == '=':
        tk.Button(root, text=button, padx=20, pady=20, font=('Helvetica', 20), command=calculate).grid(row=row_val, column=col_val)
    else:
        tk.Button(root, text=button, padx=20, pady=20, font=('Helvetica', 20), command=lambda b=button: entry.insert(tk.END, b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Run the main loop
root.mainloop()
