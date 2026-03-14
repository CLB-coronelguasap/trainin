import random
import tkinter as tk
from tkinter import messagebox
import os

# Menu Options
MENU_MAINS = ['Crunchy Taco', 'Chipotle Chicken Burrito', 'Crunchwrap Supreme', 'Nachos BellGrande', 'Soft Taco', 'Chicken Quesadilla', 'Mexican Pizza']
MENU_DRINKS = ['Pepsi', 'Diet Pepsi', 'Baja Blast', 'Mtn Dew', 'Strawberry Passionfruit Agua Refresca', 'Blue Raspberry Freeze']
MENU_SIDES = ['Cinnabon Delights', 'Fries', 'Beans and Rice', 'Beans and Cheese', 'Chips and Guac', 'Chips and Nacho Cheese']
MENU_SIZES = ['Small', 'Medium', 'Large', 'Extra Large']
MENU_SAUCES = ['Verde Salsa', 'Mild', 'Hot', 'Fire', 'Diablo', 'Nacho Cheese', 'Sour Cream', 'Creamy Jalapeño', 'Chipotle', 'Guacamole', 'Avocado Ranch', 'Spicy Ranch', 'Red']

class TacoGame:
    """Main application class for the Taco Training Game."""

    def __init__(self, root):
        self.root = root
        
        # Game State Variables
        self.target_order_requirements = {}  # Dictionary mapping item string to required quantity
        self.current_tray_items = []         # List of strings representing items the player has prepared
        self.customer_photo = None
        
        # UI Elements
        self.main_frame = tk.Frame(root)
        
        # Initialize dummy elements for static type checking (IDE compatibility)
        self.menu_frame = tk.Frame(self.main_frame)
        self.tray_listbox = tk.Listbox(self.main_frame)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        self.show_tutorial()

    def clear_main_frame(self):
        """Removes all widgets from the main frame to prepare for a new screen."""
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def show_tutorial(self):
        """Displays the tutorial screen with game instructions."""
        self.clear_main_frame()
        
        tutorial_frame = tk.Frame(self.main_frame, padx=20, pady=20)
        tutorial_frame.pack(expand=True)
        
        title_label = tk.Label(tutorial_frame, text="Taco Training Game - Tutorial", font=("Helvetica", 18, "bold"))
        title_label.pack(pady=10)
        
        instructions = (
            "Welcome to the Taco Training!\n\n"
            "Here is how to play:\n"
            "1. Read the customer's order ticket on the screen.\n"
            "2. Use the 'Menus' below to build the order.\n"
            "   (Ordering -> Mains, Drinks, Sides, Sauces)\n"
            "3. Select sizes when prompted (e.g., Sides > Fries > Large).\n"
            "4. Your prepared items will appear in your 'Current Tray'.\n"
            "5. If you make a mistake, select the item in the tray and click 'Remove'.\n"
            "6. Once the tray perfectly matches the order, click 'Serve Order'.\n\n"
            "Good luck!"
        )
        
        instructions_label = tk.Label(tutorial_frame, text=instructions, font=("Helvetica", 12), justify=tk.LEFT)
        instructions_label.pack(pady=10)
        
        start_button = tk.Button(tutorial_frame, text="Start Game", font=("Helvetica", 14), bg="#4caf50", fg="white", command=self.start_game)
        start_button.pack(pady=20)

    def generate_random_order(self):
        """Generates a random customer order and stores it in target_order_requirements."""
        self.target_order_requirements = {}
        
        # Randomly select a main item and its quantity
        num_mains = random.randint(1, 5)
        main_item = random.choice(MENU_MAINS)
        self.target_order_requirements[main_item] = self.target_order_requirements.get(main_item, 0) + num_mains
        
        # Randomly select a drink with a size
        num_drinks = random.randint(1, 2)
        drink_item = random.choice(MENU_SIZES) + ' ' + random.choice(MENU_DRINKS)
        self.target_order_requirements[drink_item] = self.target_order_requirements.get(drink_item, 0) + num_drinks
        
        # Randomly select a side with a size
        num_sides = random.randint(1, 3)
        side_item = random.choice(MENU_SIZES) + ' ' + random.choice(MENU_SIDES)
        self.target_order_requirements[side_item] = self.target_order_requirements.get(side_item, 0) + num_sides
        
        # Randomly select a sauce
        num_sauces = random.randint(1, 2)
        sauce_item = random.choice(MENU_SAUCES) + ' Sauce'
        self.target_order_requirements[sauce_item] = self.target_order_requirements.get(sauce_item, 0) + num_sauces

    def start_game(self):
        """Initializes and displays the main gameplay screen."""
        self.clear_main_frame()
        self.generate_random_order()
        self.current_tray_items = []
        
        # --- Top Frame (Customer Image + Ticket) ---
        top_frame = tk.Frame(self.main_frame, height=200, bg="#f0f0f0", bd=2, relief=tk.GROOVE)
        top_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Customer Image Section
        image_frame = tk.Frame(top_frame, bg="white", bd=2, relief=tk.SOLID)
        image_frame.pack(side=tk.LEFT, padx=10, pady=10)
        
        self.customer_photo = None
        base_dir = os.path.dirname(os.path.abspath(__file__))
        image_dir = os.path.join(base_dir, "assets", "images", "customer")
        
        if os.path.exists(image_dir):
            image_files = [file for file in os.listdir(image_dir) if file.lower().endswith(('.png', '.gif'))]
            if image_files:
                try:
                    chosen_image_path = os.path.join(image_dir, random.choice(image_files))
                    original_img = tk.PhotoImage(file=chosen_image_path)
                    self.customer_photo = original_img.subsample(2, 2) # Scale down the image
                except Exception:
                    pass
                    
        if self.customer_photo:
            customer_image_label = tk.Label(image_frame, image=self.customer_photo, bg="white")
            customer_image_label.pack(padx=5, pady=5)
        else:
            customer_image_label = tk.Label(image_frame, text="Customer\nPhoto", width=15, height=8, bg="#ccc")
            customer_image_label.pack(padx=5, pady=5)

        # Ticket Information Section
        ticket_frame = tk.Frame(top_frame, bg="#ffffe0", bd=1, relief=tk.SOLID)
        ticket_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        tk.Label(ticket_frame, text="ORDER TICKET", font=("Helvetica", 12, "bold"), bg="#ffffe0").pack()
        
        for item, count in self.target_order_requirements.items():
            tk.Label(ticket_frame, text=f"{count}x {item}", font=("Helvetica", 12), bg="#ffffe0").pack(anchor=tk.W, padx=20)
            
        # --- Bottom Frame (Interactive Menus + Player Tray) ---
        bottom_frame = tk.Frame(self.main_frame)
        bottom_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Left Side: Menus
        menu_container = tk.LabelFrame(bottom_frame, text="Menu Operations", font=("Helvetica", 10, "bold"))
        menu_container.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        
        self.menu_frame = tk.Frame(menu_container)
        self.menu_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Right Side: Tray
        tray_container = tk.LabelFrame(bottom_frame, text="Current Tray", font=("Helvetica", 10, "bold"))
        tray_container.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(5, 0))
        
        self.tray_listbox = tk.Listbox(tray_container, font=("Helvetica", 11))
        self.tray_listbox.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        button_frame = tk.Frame(tray_container)
        button_frame.pack(fill=tk.X, padx=5, pady=5)
        
        tk.Button(button_frame, text="Remove Selected", command=self.remove_selected_item).pack(side=tk.LEFT, fill=tk.X, expand=True)
        tk.Button(button_frame, text="SERVE ORDER", command=self.serve_order, bg="#2196F3", fg="white", font=("Helvetica", 10, "bold")).pack(side=tk.RIGHT, fill=tk.X, expand=True, padx=(5,0))
        
        self.show_main_category()

    def update_tray_listbox(self):
        """Refreshes the visual listbox to match the backend current_tray_items array."""
        self.tray_listbox.delete(0, tk.END)
        for item in self.current_tray_items:
            self.tray_listbox.insert(tk.END, item)

    def add_item_to_tray(self, item):
        """Adds a completed item to the tray and returns to the main menu category."""
        self.current_tray_items.append(item)
        self.update_tray_listbox()
        self.show_main_category()

    def remove_selected_item(self):
        """Removes the specific item that the user currently has selected in the listbox."""
        selected_indices = self.tray_listbox.curselection()
        if selected_indices:
            item_index = selected_indices[0]
            self.current_tray_items.pop(item_index)
            self.update_tray_listbox()

    def clear_menu_frame(self):
        """Removes all buttons from the menu frame to display a new category."""
        for widget in self.menu_frame.winfo_children():
            widget.destroy()

    def show_items_in_grid(self, item_list, click_callback, back_command):
        """Helper function to dynamically build a grid of buttons from a list of strings."""
        self.clear_menu_frame()
        tk.Button(self.menu_frame, text="< Back", command=back_command, bg="#ffcccc").grid(row=0, column=0, columnspan=3, sticky="we", pady=5, padx=5)
        
        # Distribute available space evenly among 3 columns
        self.menu_frame.columnconfigure(0, weight=1)
        self.menu_frame.columnconfigure(1, weight=1)
        self.menu_frame.columnconfigure(2, weight=1)

        row_index = 1
        col_index = 0
        for item_name in item_list:
            tk.Button(self.menu_frame, text=item_name, command=lambda name=item_name: click_callback(name)).grid(row=row_index, column=col_index, sticky="we", padx=2, pady=2)
            
            col_index += 1
            # Move to the next row after 3 items
            if col_index > 2:
                col_index = 0
                row_index += 1

    def show_main_category(self):
        """Displays the root level menus: Mains, Drinks, Sides & Sauces."""
        self.clear_menu_frame()
        tk.Button(self.menu_frame, text="Ordering (Mains)", command=self.show_mains_menu, font=("Helvetica", 12), height=2).pack(fill=tk.X, pady=5)
        tk.Button(self.menu_frame, text="Drinks", command=self.show_drinks_menu, font=("Helvetica", 12), height=2).pack(fill=tk.X, pady=5)
        tk.Button(self.menu_frame, text="Sides & Sauces", command=self.show_sides_main_menu, font=("Helvetica", 12), height=2).pack(fill=tk.X, pady=5)

    def show_mains_menu(self):
        self.show_items_in_grid(MENU_MAINS, self.add_item_to_tray, self.show_main_category)

    def show_drinks_menu(self):
        self.show_items_in_grid(MENU_DRINKS, lambda drink: self.show_sizes_menu(drink, 'drink'), self.show_main_category)

    def show_sides_main_menu(self):
        """Displays the intermediate menu separating food sides and sauces."""
        self.clear_menu_frame()
        tk.Button(self.menu_frame, text="< Back", command=self.show_main_category, bg="#ffcccc").pack(fill=tk.X, pady=5)
        tk.Button(self.menu_frame, text="Food Sides", command=self.show_food_sides_menu, font=("Helvetica", 12), height=2).pack(fill=tk.X, pady=5)
        tk.Button(self.menu_frame, text="Sauces", command=self.show_sauces_menu, font=("Helvetica", 12), height=2).pack(fill=tk.X, pady=5)

    def show_food_sides_menu(self):
        self.show_items_in_grid(MENU_SIDES, lambda side: self.show_sizes_menu(side, 'side'), self.show_sides_main_menu)

    def show_sauces_menu(self):
        # Sauces don't need a size, they immediately get added to the tray with the word "Sauce" appended
        self.show_items_in_grid(MENU_SAUCES, lambda sauce: self.add_item_to_tray(f"{sauce} Sauce"), self.show_sides_main_menu)

    def show_sizes_menu(self, base_item, category):
        """Shows size selection after choosing a drink or a side."""
        # Determine where the "Back" button should return based on the category
        back_cmd = self.show_drinks_menu if category == 'drink' else self.show_food_sides_menu
        self.show_items_in_grid(MENU_SIZES, lambda size_option: self.add_item_to_tray(f"{size_option} {base_item}"), back_cmd)

    def serve_order(self):
        """Validates the current tray against the target order ticket requirements."""
        tray_counts = {}
        # Count the frequency of each item currently in the tray
        for item in self.current_tray_items:
            tray_counts[item] = tray_counts.get(item, 0) + 1
            
        # Check if the generated tray perfectly matches the generated ticket counts
        if tray_counts == self.target_order_requirements:
            messagebox.showinfo("Success", "Perfect! The customer is happy.")
            self.start_game()
        else:
            messagebox.showerror("Error", "The order is incorrect. Please fix it or try again.")

def start_training(root):
    """Entry point function called by main.py to begin the game within the window."""
    # Clear out any previous frames from the main menu
    for widget in root.winfo_children():
        widget.destroy()
        
    app = TacoGame(root)
    # Keep a reference to prevent the garbage collector from destroying the game logic instance
    root.taco_game_app = app

if __name__ == "__main__":
    # Test block to run training.py on its own without main.py
    root = tk.Tk()
    root.title("Taco Training Game")
    root.geometry("800x600")
    start_training(root)
    root.mainloop()
