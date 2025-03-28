import tkinter as tk
from tkinter import messagebox  # for showing error message
import string
import secrets #More secure than random for password generation
import pyperclip   #Copies password to the clipboard
import threading  #to auto clear clipboard
import time

                             #create a mian GUI for window____________________

root = tk.Tk()     #creating the main window
root.title("Super Secure Password Generator")
root.geometry("400x500") #window size
root.config(bg="#121212")  # Dark theme background
                                       #function to generate password______________
print("Choose which you want to include in password: ")
use_upper = tk.BooleanVar(value=True)
use_lower = tk.BooleanVar(value=True)
use_numbers = tk.BooleanVar(value=True)
use_symbols = tk.BooleanVar(value=True)

chk_upper = tk.Checkbutton(root, text="Include Uppercase", variable=use_upper, bg="#1e1e1e", fg="white", selectcolor="#1e1e1e")
chk_lower = tk.Checkbutton(root, text="Include Lowercase", variable=use_lower, bg="#1e1e1e", fg="white", selectcolor="#1e1e1e")
chk_numbers = tk.Checkbutton(root, text="Include Numbers", variable=use_numbers, bg="#1e1e1e", fg="white", selectcolor="#1e1e1e")
chk_symbols = tk.Checkbutton(root, text="Include Symbols", variable=use_symbols, bg="#1e1e1e", fg="white", selectcolor="#1e1e1e")

chk_upper.pack(pady=2)
chk_lower.pack(pady=2)
chk_numbers.pack(pady=2)
chk_symbols.pack(pady=2)


                                     #Add Input Field for Password Length__________________

tk.Label(root, text="Password Length (8-64):", bg="#1e1e1e", fg="white").pack(pady=(10,2)) # input field text label
length_entry = tk.Entry(root)   #text label for input feild
length_entry.insert(0, "12")  # Default length
length_entry.pack(pady=(0,10))
                                      #password display field_____________________

password_var = tk.StringVar() # store the generated password
password_display = tk.Entry(root, textvariable=password_var, width=30, font=('Arial', 14)) #display generated password in input field
password_display.pack(pady=10)
                                     #strenth indicator__________________

strength_label = tk.Label(root, text="Strength: ", bg="#1e1e1e", fg="white")
strength_label.pack(pady=5)

                                      #Function to Check Password Strength___________

def check_strength(pw):
    score = 0
    if len(pw) >= 12:
        score += 1
    if any(c.islower() for c in pw):
        score += 1
    if any(c.isupper() for c in pw):
        score += 1
    if any(c.isdigit() for c in pw):
        score += 1
    if any(c in string.punctuation for c in pw):
        score += 1
    
    if score <= 2:
        strength_label.config(text="Strength: Weak", fg="red")
    elif score == 3 or score == 4:
        strength_label.config(text="Strength: Moderate", fg="orange")
    else:
        strength_label.config(text="Strength: Strong", fg="green")


                                        #Function to Clear Clipboard After 10 Sec___________________

def clear_clipboard():
    time.sleep(10)    #wait a 10 sec before clearing clpboard
    pyperclip.copy('')
    print("Clipboard cleared!")

                                       #password generation function____________________

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 8 or length > 64:
            messagebox.showerror("Error", "Length must be between 8 and 64")
            return
        
        chars = ''
        if use_upper.get():
            chars += string.ascii_uppercase
        if use_lower.get():
            chars += string.ascii_lowercase
        if use_numbers.get():
            chars += string.digits
        if use_symbols.get():
            chars += string.punctuation
        
        if not chars:
            messagebox.showerror("Error", "Select at least one character set!")
            return
        
        password = ''.join(secrets.choice(chars) for _ in range(length)) #Uses secrets.choice() for randomness
        password_var.set(password)
        check_strength(password)
        pyperclip.copy(password) # copy password to clipboard
        threading.Thread(target=clear_clipboard, daemon=True).start()
    except ValueError:
        messagebox.showerror("Error", "Invalid length!")


                                             #generate button______________

generate_btn = tk.Button(root, text="Generate button", command=generate_password, bg="#0f62fe", fg="white", font=("Arial", 12, "bold"), 
relief="raised", activebackground="#0047ab")
generate_btn.pack(pady=10)



                                             # generate key shortcut___________________

root.bind('<Control-g>', lambda event: generate_password())


                                              #Run___________-
root.mainloop()







