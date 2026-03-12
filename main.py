import tkinter as tk
from tkinter import messagebox
import settings_menu
import training

# ASCII Art Banner using a recognizable format
TACO_BELL_BANNER = r"""
 _______       _____ ____  ____  ______ _      _      
|__   __|/\   / ____/ __ \|  _ \|  ____| |    | |     
   | |  /  \ | |   | |  | | |_\) | |__  | |    | |     
   | | / /\ \| |   | |  | |  _ <|  __| | |    | |     
   | |/ ____ \ |___| |__| | |_\) | |____| |____| |____ 
   |_/_/    \_\_____\____/|____/|______|______|______|
"""

def show_login_screen():
    # Clear the window
    for widget in root.winfo_children():
        widget.destroy()

    # Create frames to center the login box
    top_spacer = tk.Frame(root)
    top_spacer.pack(expand=True)

    login_frame = tk.Frame(root, bd=2, relief=tk.RAISED, padx=40, pady=40)
    login_frame.pack(expand=False)

    bottom_spacer = tk.Frame(root)
    bottom_spacer.pack(expand=True)

    tk.Label(login_frame, text="Taco Bell Simulator Login", font=("Helvetica", 24)).pack(pady=20)

    tk.Label(login_frame, text="Username:", font=("Helvetica", 16)).pack(pady=5)
    username_entry = tk.Entry(login_frame, font=("Helvetica", 16))
    username_entry.pack(pady=5)

    tk.Label(login_frame, text="Password:", font=("Helvetica", 16)).pack(pady=5)
    password_entry = tk.Entry(login_frame, show="*", font=("Helvetica", 16))
    password_entry.pack(pady=5)

    def attempt_login():
        if username_entry.get() == "admin" and password_entry.get() == "password":
            show_main_menu()
        else:
            messagebox.showerror("Error", "Invalid username or password")

    tk.Button(login_frame, text="Login", font=("Helvetica", 16), command=attempt_login, width=15).pack(pady=20)
    
    # Allow user to quit via Escape key
    tk.Button(root, text="Exit Simulator", font=("Helvetica", 12), command=root.destroy).pack(side=tk.BOTTOM, pady=20)


def show_main_menu():
    # Clear the window
    for widget in root.winfo_children():
        widget.destroy()

    # Top half: Banner
    top_frame = tk.Frame(root)
    top_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    # Use a generic Courier font to display ASCII accurately
    banner_label = tk.Label(top_frame, text=TACO_BELL_BANNER, font=("Courier", 18, "bold"), justify=tk.LEFT)
    banner_label.pack(expand=True)

    # Bottom half: Buttons
    bottom_frame = tk.Frame(root)
    bottom_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    buttons_frame = tk.Frame(bottom_frame)
    buttons_frame.pack(expand=True)

    tk.Button(buttons_frame, text="Start Training", font=("Helvetica", 18), width=20, command=start_training).pack(pady=10)
    tk.Button(buttons_frame, text="Settings", font=("Helvetica", 18), width=20, command=settings).pack(pady=10)
    tk.Button(buttons_frame, text="Exit", font=("Helvetica", 18), width=20, command=root.destroy).pack(pady=10)


def start_training():
    training.start_training(root)


def settings():
    settings_menu.show_settings_menu(root, show_main_menu)


if __name__ == "__main__":
    # Initialize App
    root = tk.Tk()
    root.title("Taco Bell Training Simulator")

    # Fullscreen setup
    root.attributes('-fullscreen', True)
    
    # Allow exiting fullscreen for debugging convenience
    root.bind("<Escape>", lambda e: root.attributes('-fullscreen', False))
    root.bind("<F11>", lambda e: root.attributes('-fullscreen', not root.attributes('-fullscreen')))

    # Start with login screen
    show_login_screen()

    # Start main application loop
    root.mainloop()

