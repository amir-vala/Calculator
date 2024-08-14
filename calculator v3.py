# calculator_v3.py
import tkinter as tk
from math import sqrt, sin, cos, tan, log

def evaluate_expression(expression):
    try:
        result = str(eval(expression))
        return result
    except Exception as e:
        return "Error"

def on_button_click(button_text):
    current_text = entry.get()
    new_text = current_text + button_text
    entry.delete(0, tk.END)
    entry.insert(0, new_text)

def on_clear():
    entry.delete(0, tk.END)

def on_equals():
    expression = entry.get()
    result = evaluate_expression(expression)
    entry.delete(0, tk.END)
    entry.insert(0, result)

def on_sqrt():
    current_text = entry.get()
    try:
        result = str(sqrt(float(current_text)))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def on_function(func):
    current_text = entry.get()
    try:
        result = str(func(float(current_text)))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Advanced Calculator")

entry = tk.Entry(root, width=20, font=('Arial', 24), bd=8, insertwidth=4, justify='right')
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
    action = lambda x=button: on_button_click(x)
    tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 18), command=action).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

tk.Button(root, text='C', padx=20, pady=20, font=('Arial', 18), command=on_clear).grid(row=row_val, column=0)
tk.Button(root, text='√', padx=20, pady=20, font=('Arial', 18), command=on_sqrt).grid(row=row_val, column=1)
tk.Button(root, text='sin', padx=20, pady=20, font=('Arial', 18), command=lambda: on_function(sin)).grid(row=row_val, column=2)
tk.Button(root, text='cos', padx=20, pady=20, font=('Arial', 18), command=lambda: on_function(cos)).grid(row=row_val, column=3)
row_val += 1
tk.Button(root, text='tan', padx=20, pady=20, font=('Arial', 18), command=lambda: on_function(tan)).grid(row=row_val, column=0)
tk.Button(root, text='log', padx=20, pady=20, font=('Arial', 18), command=lambda: on_function(log)).grid(row=row_val, column=1)

root.mainloop()
