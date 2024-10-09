from tkinter import *
import os
from tkinter import messagebox

root = Tk()
root.geometry("325x200")
root.title("PC-Functions")

# Function to create sky blue gradient background
def gradient_color(steps):
    color1 = [135, 206, 235]  # RGB for light sky blue (#87ceeb)
    color2 = [70, 130, 180]   # RGB for steel blue (#4682b4)
    
    for i in range(steps):
        r = int(color1[0] + (color2[0] - color1[0]) * i / steps)
        g = int(color1[1] + (color2[1] - color1[1]) * i / steps)
        b = int(color1[2] + (color2[2] - color1[2]) * i / steps)
        color = f'#{r:02x}{g:02x}{b:02x}'  # Convert RGB to hex
        root.config(bg=color)
        root.update_idletasks()  # Force update of the window

# Setting up fonts
f = ('Agency FB', 15, 'bold')
f1 = ('Agency FB', 15, 'bold')

# Functions for system commands
def shutdown():
    if messagebox.askyesno("Confirm Shutdown", "Are you sure you want to shutdown?"):
        os.system("shutdown /s /t 0")

def restart():
    if messagebox.askyesno("Confirm Restart", "Are you sure you want to restart?"):
        os.system("shutdown /r /t 0")

def logout():
    if messagebox.askyesno("Confirm Logout", "Are you sure you want to log out?"):
        os.system("shutdown /l")

# Apply the gradient background (call the function with 100 steps)
gradient_color(100)

# Create buttons and labels
lb1 = Label(root, text='Shutdown, Restart or Logout', font=f1, bg='#87ceeb', fg='white')
lb1.pack(pady=5)

Button(root, text='Shutdown', font=f, bg='#333333', fg='white', command=shutdown).pack(pady=5)
Button(root, text='Restart', font=f, bg='#333333', fg='white', command=restart).pack(pady=5)
Button(root, text='Logout', font=f, bg='#333333', fg='white', command=logout).pack(pady=
