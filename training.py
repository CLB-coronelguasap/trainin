import random
import time
import tkinter as tk
import os

food = ['Crunchy Taco', 'Chipotle Chicken Burrito', 'Crunchwrap Supreme', 'Nachos BellGrande', 'Soft Taco', 'Chicken Quesadilla', 'Mexican Pizza']
drinks = ['Pepsi', 'Diet Pepsi', 'Baja Blast', 'Mtn Dew', 'Strawberry Passionfruit Agua Refresca', 'Blue Raspberry Freeze']
sides = ['Cinnabon Delights', 'Fries', 'Beans and Rice', 'Beans and Cheese', 'Chips and Guac', 'Chips and Nacho Cheese']
sizes = ['Small', 'Medium', 'Large']
sauces = ['Verde Salsa', 'Mild', 'Hot', 'Fire', 'Diablo', 'Nacho Cheese', 'Sour Cream', 'Creamy Jalapeño', 'Chipotle', 'Guacamole', 'Avocado Ranch', 'Spicy Ranch', 'Red']

print(str(random.randint(1,5)) + 'x ' + random.choice(food))
print(str(random.randint(1,2)) + 'x ' + random.choice(sizes) + ' ' + random.choice(drinks))
print(str(random.randint(1,3)) + 'x ' + random.choice(sizes) + ' ' + random.choice(sides))
print(str(random.randint(1,2)) + 'x ' + random.choice(sauces) + ' Sauce')

def start_training(root, on_back):
    for widget in root.winfo_children():
        widget.destroy()
    
    game_frame = tk.Frame(root)
    game_frame.pack(expand=True)
    
