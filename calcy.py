import tkinter as tk

def on_button_click(value):
    current_text = entry_var.get()
    if value == "C":
        entry_var.set("")
    elif value == "=":
        try:
            entry_var.set(eval(current_text))
        except Exception:
            entry_var.set("Error")
    else:
        entry_var.set(current_text + str(value))

# Create main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.configure(bg="black")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), bd=10, relief=tk.FLAT, bg="black", fg="white")
entry.pack(fill=tk.BOTH, ipadx=8, ipady=8, padx=10, pady=10)

buttons_frame = tk.Frame(root, bg="black")
buttons_frame.pack()

buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('C', '0', '=', '+')
]

for row in buttons:
    row_frame = tk.Frame(buttons_frame, bg="black")
    row_frame.pack(side=tk.TOP, fill=tk.BOTH)
    for char in row:
        button = tk.Button(
            row_frame, text=char, font=("Arial", 18), width=5, height=2,
            bg="black", fg="white", relief=tk.GROOVE,
            command=lambda value=char: on_button_click(value)
        )
        button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

root.mainloop()
