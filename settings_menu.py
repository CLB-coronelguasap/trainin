import tkinter as tk
from tkinter import messagebox

def show_settings_menu(root, on_back):
    # Clear the window
    for widget in root.winfo_children():
        widget.destroy()

    # Title
    tk.Label(root, text="Settings Menu", font=("Helvetica", 36, "bold")).pack(pady=40)

    # Frame for settings
    settings_frame = tk.Frame(root)
    settings_frame.pack(expand=True)

    # Audio Volume
    tk.Label(settings_frame, text="Audio Volume:", font=("Helvetica", 18)).grid(row=0, column=0, padx=20, pady=20, sticky="e")
    volume_scale = tk.Scale(settings_frame, from_=0, to=100, orient=tk.HORIZONTAL, length=300, font=("Helvetica", 14))
    volume_scale.set(75)
    volume_scale.grid(row=0, column=1, padx=20, pady=20)

    # Difficulty Level
    tk.Label(settings_frame, text="Difficulty Level:", font=("Helvetica", 18)).grid(row=1, column=0, padx=20, pady=20, sticky="e")
    difficulty_var = tk.StringVar(value="Normal")
    difficulty_menu = tk.OptionMenu(settings_frame, difficulty_var, "Beginner", "Intermediate", "Hard", "Expert")
    difficulty_menu.config(font=("Helvetica", 14), width=18)
    difficulty_menu.grid(row=1, column=1, padx=20, pady=20, sticky="w")

    # Shift Duration
    tk.Label(settings_frame, text="Shift Duration:", font=("Helvetica", 18)).grid(row=2, column=0, padx=20, pady=20, sticky="e")
    shift_var = tk.StringVar(value="8 Hours")
    shift_menu = tk.OptionMenu(settings_frame, shift_var, "4 Hours", "6 Hours", "8 Hours", "12 Hours (Double Shift)")
    shift_menu.config(font=("Helvetica", 14), width=18)
    shift_menu.grid(row=2, column=1, padx=20, pady=20, sticky="w")

    # Fullscreen Toggle
    fullscreen_var = tk.BooleanVar(value=root.attributes('-fullscreen'))
    def toggle_fullscreen():
        root.attributes('-fullscreen', fullscreen_var.get())

    tk.Checkbutton(
        settings_frame, 
        text="Fullscreen Mode", 
        variable=fullscreen_var, 
        command=toggle_fullscreen,
        font=("Helvetica", 18)
    ).grid(row=3, column=0, columnspan=2, pady=30)

    # Apply & Back Buttons container
    btn_frame = tk.Frame(root)
    btn_frame.pack(side=tk.BOTTOM, pady=50)

    def saved_prompt():
        messagebox.showinfo("Settings", "Settings applied successfully!")

    tk.Button(btn_frame, text="Apply Settings", font=("Helvetica", 18), width=20, bg="#4CAF50", fg="white", command=saved_prompt).pack(side=tk.LEFT, padx=10)
    tk.Button(btn_frame, text="Back to Main Menu", font=("Helvetica", 18), width=20, command=on_back).pack(side=tk.LEFT, padx=10)
