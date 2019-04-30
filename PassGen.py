# We need to generate a random string of a fixed length.
# Generate a random alphanumeric string with letters and numbers.
# Generate a random string which contains uppercase and lowercase letters, digits, and special characters.
# Generate a random password.
# Use the SystemRandom method to generate a secure random string for 
# the sensitive application.

import Tkinter as tk
from Tkinter import *
import random
import string

Ht = 300
Wd = 450

root = tk.Tk()

sR = random.SystemRandom()

strings = string.ascii_letters + string.digits + string.punctuation
def random_pass():
	x = strings
	password = random.choice(string.ascii_lowercase)
	password += random.choice(string.ascii_uppercase)
	password += random.choice(string.digits)
	password += random.choice(string.punctuation)

	for i in range(8):
		password += sR.choice(x)
		entry = tk.Entry(root, state='readonly')
		var = tk.StringVar()
		var.set(password)
		entry.configure(textvariable=var, relief='sunken', font=40)
		entry.place(relx=0.375, rely=.5, relwidth=0.25, relheight=0.15)
	print(password)

	
canvas = tk.Canvas(root, height=Ht, width=Wd)
canvas.pack()

background_image = tk.PhotoImage(file='IMG_1419.gif')

background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

frame = tk.Frame(root, bg='black', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.4, relheight=0.1, anchor='n')

button = tk.Button(frame, text="Generate a password!", command=random_pass, bg='gray')
button.place(relx=0.015, relwidth=.96, relheight=1)

root.resizable(False, False)

root.mainloop()



