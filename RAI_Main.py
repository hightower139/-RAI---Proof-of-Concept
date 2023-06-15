import tkinter as tk
from tkinter import messagebox

def show_message():
    if check_state.get() == 0:
        print(textbox.get('1.0', tk.END))
    else:
        messagebox.showinfo(title='Message', message=textbox.get('1.0', tk.END))

root = tk.Tk()
root.title('RAI - Proof of Concept')
root.iconbitmap("myIcon.ico")

label = tk.Label(root, text='Your Message', font=('Arial', 18))
label.pack(padx=10, pady=10)

textbox = tk.Text(root, height=5, font=('Arial', 16))
textbox.pack(padx=10, pady=10)

check_state = tk.IntVar()

checkbox = tk.Checkbutton(root, text='Show Message Box', font=('Arial', 16), variable=check_state)
checkbox.pack(padx=10, pady=10)

button = tk.Button(root, text='Show Message', font=('Arial', 18), command=show_message)
button.pack(padx=10, pady=10)

root.mainloop()