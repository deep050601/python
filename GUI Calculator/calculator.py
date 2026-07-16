import tkinter as tk


def click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))


def clear():
    entry.delete(0, tk.END)


def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


# Main Window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

# Entry Box
entry = tk.Entry(root, width=20, font=("Arial", 20), borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Buttons
buttons = [
    ("7", 1, 0),
    ("8", 1, 1),
    ("9", 1, 2),
    ("/", 1, 3),
    ("4", 2, 0),
    ("5", 2, 1),
    ("6", 2, 2),
    ("*", 2, 3),
    ("1", 3, 0),
    ("2", 3, 1),
    ("3", 3, 2),
    ("-", 3, 3),
    ("0", 4, 0),
    (".", 4, 1),
    ("=", 4, 2),
    ("+", 4, 3),
]

for text, row, col in buttons:
    if text == "=":
        btn = tk.Button(
            root, text=text, padx=20, pady=20, font=("Arial", 14), command=calculate
        )
    else:
        btn = tk.Button(
            root,
            text=text,
            padx=20,
            pady=20,
            font=("Arial", 14),
            command=lambda t=text: click(t),
        )

    btn.grid(row=row, column=col)

# Clear Button
clear_btn = tk.Button(
    root, text="AC", padx=20, pady=20, font=("Arial", 14), command=clear
)

clear_btn.grid(row=5, column=0, columnspan=4, sticky="we")

root.mainloop()
