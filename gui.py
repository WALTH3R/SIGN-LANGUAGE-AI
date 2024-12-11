import tkinter as tk
from tkinter import messagebox
import os
from data_collection import collect_data
from gui import live_translation
from model import train_model

def start_data_collection():
    sign = sign_var.get()
    if not sign:
        messagebox.showerror("Error", "Please enter a sign name.")
        return
    collect_data(sign)
    messagebox.showinfo("Info", f"Data collection for '{sign}' complete.")

def start_model_training():
    # Load data here (implement as needed)
    X, y = load_data()  # Replace with your data loading function
    train_model(X, y)
    messagebox.showinfo("Info", "Model training complete.")

def start_live_translation():
    live_translation()

# GUI Setup
root = tk.Tk()
root.title("Sign Language Translator")

# Data Collection Section
tk.Label(root, text="Sign Name:").grid(row=0, column=0, padx=10, pady=5)
sign_var = tk.StringVar()
tk.Entry(root, textvariable=sign_var).grid(row=0, column=1, padx=10, pady=5)
tk.Button(root, text="Start Data Collection", command=start_data_collection).grid(row=0, column=2, padx=10, pady=5)

# Model Training Section
tk.Button(root, text="Train Model", command=start_model_training).grid(row=1, column=0, columnspan=3, pady=10)

# Live Translation Section
tk.Button(root, text="Start Live Translation", command=start_live_translation).grid(row=2, column=0, columnspan=3, pady=10)

root.mainloop()
