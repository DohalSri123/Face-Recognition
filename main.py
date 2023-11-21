import os
import webbrowser
import tkinter as tk
from tkinter import ttk

import threading

def take():
    threading.Thread(target=os.system, args=("python attendance_taker.py",)).start()

def convert():
    threading.Thread(target=os.system, args=("python features_extraction_to_csv.py",)).start()

def register():
    threading.Thread(target=os.system, args=("python get_faces_from_camera_tkinter.py",)).start()

def view():
    threading.Thread(target=os.system, args=("python app.py",)).start()
    threading.Thread(target=webbrowser.open_new, args=("http://127.0.0.1:5000",)).start()


root = tk.Tk()
root.geometry('400x300')
root.resizable(True, True)
root.title('VIT-AP')

take_button = ttk.Button(root, text="Take Attendance", command=take)
register_button = ttk.Button(root, text="Register", command=register)
convert_button = ttk.Button(root, text="Update", command=convert)
view_button = ttk.Button(root, text="View Attendance", command=view)

take_button.pack(padx=8, pady=8)
convert_button.pack(padx=8, pady=8)
register_button.pack(padx=8, pady=8)
view_button.pack(padx=8, pady=8)

root.mainloop()