import random
import tkinter as tk
from tkinter import messagebox
import os

import random
import tkinter as tk
from tkinter import messagebox
import os

food = ['Crunchy Taco', 'Chipotle Chicken Burrito', 'Crunchwrap Supreme', 'Nachos BellGrande', 'Soft Taco', 'Chicken Quesadilla', 'Mexican Pizza']
drinks = ['Pepsi', 'Diet Pepsi', 'Baja Blast', 'Mtn Dew', 'Strawberry Passionfruit Agua Refresca', 'Blue Raspberry Freeze']
sides = ['Cinnabon Delights', 'Fries', 'Beans and Rice', 'Beans and Cheese', 'Chips and Guac', 'Chips and Nacho Cheese']
sizes = ['Small', 'Medium', 'Large', 'Extra Large']
sauces = ['Verde Salsa', 'Mild', 'Hot', 'Fire', 'Diablo', 'Nacho Cheese', 'Sour Cream', 'Creamy Jalapeño', 'Chipotle', 'Guacamole', 'Avocado Ranch', 'Spicy Ranch', 'Red']

class TacoGame:
    def __init__(self, root):
        self.root = root
        
        self.ticket_counts = {}
        self.tray_items = []
        self.customer_photo = None
        self.menu_frame = None
        self.tray_listbox = None
        
        # UI Elements
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        self.show_tutorial()

    def clear_main_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def show_tutorial(self):
        self.clear_main_frame()
        
        tut_frame = tk.Frame(self.main_frame, padx=20, pady=20)
        tut_frame.pack(expand=True)
        
        title = tk.Label(tut_frame, text="Taco Training Game - Tutorial", font=("Helvetica", 18, "bold"))
        title.pack(pady=10)
        
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
        
        lbl = tk.Label(tut_frame, text=instructions, font=("Helvetica", 12), justify=tk.LEFT)
        lbl.pack(pady=10)
        
        btn = tk.Button(tut_frame, text="Start Game", font=("Helvetica", 14), bg="#4caf50", fg="white", command=self.start_game)
        btn.pack(pady=20)

    def generate_order(self):
        self.ticket_counts = {}
        
        # Mains
        num_mains = random.randint(1,5)
        main_item = random.choice(food)
        self.ticket_counts[main_item] = self.ticket_counts.get(main_item, 0) + num_mains
        
        # Drinks
        num_drinks = random.randint(1,2)
        drink_item = random.choice(sizes) + ' ' + random.choice(drinks)
        self.ticket_counts[drink_item] = self.ticket_counts.get(drink_item, 0) + num_drinks
        
        # Sides
        num_sides = random.randint(1,3)
        side_item = random.choice(sizes) + ' ' + random.choice(sides)
        self.ticket_counts[side_item] = self.ticket_counts.get(side_item, 0) + num_sides
        
        # Sauces
        num_sauces = random.randint(1,2)
        sauce_item = random.choice(sauces) + ' Sauce'
        self.ticket_counts[sauce_item] = self.ticket_counts.get(sauce_item, 0) + num_sauces

    def start_game(self):
        self.clear_main_frame()
        self.generate_order()
        self.tray_items = []
        
        # Top Frame (Customer + Ticket)
        top_frame = tk.Frame(self.main_frame, height=200, bg="#f0f0f0", bd=2, relief=tk.GROOVE)
        top_frame.pack(fill=tk.X, padx=10, pady=10)
        
        # Customer Image
        img_frame = tk.Frame(top_frame, bg="white", bd=2, relief=tk.SOLID)
        img_frame.pack(side=tk.LEFT, padx=10, pady=10)
        
        self.customer_photo = None
        base_dir = os.path.dirname(os.path.abspath(__file__))
        img_dir = os.path.join(base_dir, "assets", "images", "customer")
        
        if os.path.exists(img_dir):
            images = [f for f in os.listdir(img_dir) if f.lower().endswith(('.png', '.gif'))]
            if images:
                try:
                    img_path = os.path.join(img_dir, random.choice(images))
                    original_img = tk.PhotoImage(file=img_path)
                    self.customer_photo = original_img.subsample(2, 2)
                except Exception as e:
                    pass
                    
        if self.customer_photo:
            lbl_img = tk.Label(img_frame, image=self.customer_photo, bg="white")
            lbl_img.pack(padx=5, pady=5)
        else:
            lbl_img = tk.Label(img_frame, text="Customer\nPhoto", width=15, height=8, bg="#ccc")
            lbl_img.pack(padx=5, pady=5)

        # Ticket Information
        ticket_frame = tk.Frame(top_frame, bg="#ffffe0", bd=1, relief=tk.SOLID)
        ticket_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        tk.Label(ticket_frame, text="ORDER TICKET", font=("Helvetica", 12, "bold"), bg="#ffffe0").pack()
        
        for item, count in self.ticket_counts.items():
            tk.Label(ticket_frame, text=f"{count}x {item}", font=("Helvetica", 12), bg="#ffffe0").pack(anchor=tk.W, padx=20)
            
        # Bottom Frame (Menus + Tray)
        bottom_frame = tk.Frame(self.main_frame)
        bottom_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Menus
        menu_container = tk.LabelFrame(bottom_frame, text="Menu Operations", font=("Helvetica", 10, "bold"))
        menu_container.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        
        self.menu_frame = tk.Frame(menu_container)
        self.menu_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Tray
        tray_container = tk.LabelFrame(bottom_frame, text="Current Tray", font=("Helvetica", 10, "bold"))
        tray_container.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(5, 0))
        
        self.tray_listbox = tk.Listbox(tray_container, font=("Helvetica", 11))
        self.tray_listbox.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        btn_frame = tk.Frame(tray_container)
        btn_frame.pack(fill=tk.X, padx=5, pady=5)
        
        tk.Button(btn_frame, text="Remove Selected", command=self.remove_item).pack(side=tk.LEFT, fill=tk.X, expand=True)
        tk.Button(btn_frame, text="SERVE ORDER", command=self.serve_order, bg="#2196F3", fg="white", font=("Helvetica", 10, "bold")).pack(side=tk.RIGHT, fill=tk.X, expand=True, padx=(5,0))
        
        self.show_main_category()

    def update_tray_listbox(self):
        self.tray_listbox.delete(0, tk.END)
        for item in self.tray_items:
            self.tray_listbox.insert(tk.END, item)

    def add_to_tray(self, item):
        self.tray_items.append(item)
        self.update_tray_listbox()
        self.show_main_category()  # return to root menu

    def remove_item(self):
        sel = self.tray_listbox.curselection()
        if sel:
            idx = sel[0]
            self.tray_items.pop(idx)
            self.update_tray_listbox()

    def clear_menu(self):
        for widget in self.menu_frame.winfo_children():
            widget.destroy()

    def show_items_in_grid(self, items, callback, back_command):
        self.clear_menu()
        tk.Button(self.menu_frame, text="< Back", command=back_command, bg="#ffcccc").grid(row=0, column=0, columnspan=3, sticky="we", pady=5, padx=5)
        
        self.menu_frame.columnconfigure(0, weight=1)
        self.menu_frame.columnconfigure(1, weight=1)
        self.menu_frame.columnconfigure(2, weight=1)

        r = 1
        c = 0
        for item in items:
            tk.Button(self.menu_frame, text=item, command=lambda i=item: callback(i)).grid(row=r, column=c, sticky="we", padx=2, pady=2)
            c += 1
            if c > 2:
                c = 0
                r += 1

    def show_main_category(self):
        self.clear_menu()
        tk.Button(self.menu_frame, text="Ordering (Mains)", command=self.show_mains, font=("Helvetica", 12), height=2).pack(fill=tk.X, pady=5)
        tk.Button(self.menu_frame, text="Drinks", command=self.show_drinks, font=("Helvetica", 12), height=2).pack(fill=tk.X, pady=5)
        tk.Button(self.menu_frame, text="Sides & Sauces", command=self.show_sides_main, font=("Helvetica", 12), height=2).pack(fill=tk.X, pady=5)

    def show_mains(self):
        self.show_items_in_grid(food, self.add_to_tray, self.show_main_category)

    def show_drinks(self):
        self.show_items_in_grid(drinks, lambda d: self.show_sizes(d, 'drink'), self.show_main_category)

    def show_sides_main(self):
        self.clear_menu()
        tk.Button(self.menu_frame, text="< Back", command=self.show_main_category, bg="#ffcccc").pack(fill=tk.X, pady=5)
        tk.Button(self.menu_frame, text="Food Sides", command=self.show_sides_food, font=("Helvetica", 12), height=2).pack(fill=tk.X, pady=5)
        tk.Button(self.menu_frame, text="Sauces", command=self.show_sauces, font=("Helvetica", 12), height=2).pack(fill=tk.X, pady=5)

    def show_sides_food(self):
        self.show_items_in_grid(sides, lambda s: self.show_sizes(s, 'side'), self.show_sides_main)

    def show_sauces(self):
        self.show_items_in_grid(sauces, lambda s: self.add_to_tray(f"{s} Sauce"), self.show_sides_main)

    def show_sizes(self, base_item, category):
        back_cmd = self.show_drinks if category == 'drink' else self.show_sides_food
        self.show_items_in_grid(sizes, lambda sz: self.add_to_tray(f"{sz} {base_item}"), back_cmd)

    def serve_order(self):
        tray_counts = {}
        for item in self.tray_items:
            tray_counts[item] = tray_counts.get(item, 0) + 1
            
        if tray_counts == self.ticket_counts:
            messagebox.showinfo("Success", "Perfect! The customer is happy.")
            self.start_game()
        else:
            messagebox.showerror("Error", "The order is incorrect. Please fix it or try again.")

def start_training(root):
    for widget in root.winfo_children():
        widget.destroy()
    app = TacoGame(root)
    # keep a reference to prevent garbage collection
    root.taco_game_app = app

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Taco Training Game")
    root.geometry("800x600")
    start_training(root)
    root.mainloop()
