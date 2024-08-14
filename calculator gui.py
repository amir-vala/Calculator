# calculator_gui.py

import tkinter as tk

def on_click(operation):
    try:
        result = eval(operation)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def append_to_entry(text):
    entry.insert(tk.END, text)

def clear_entry():
    entry.delete(0, tk.END)

app = tk.Tk()
app.title("Simple Calculator")

entry = tk.Entry(app, width=16, font=('Arial', 24), bd=8, insertwidth=4, bg="powder blue", justify='right')
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    action = lambda x=button: append_to_entry(x) if x != '=' else on_click(entry.get())
    tk.Button(app, text=button, padx=20, pady=20, bd=8, fg="black", font=('Arial', 18), command=action).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

tk.Button(app, text='C', padx=20, pady=20, bd=8, fg="black", font=('Arial', 18), command=clear_entry).grid(row=row_val, column=0, columnspan=4)

app.mainloop()
