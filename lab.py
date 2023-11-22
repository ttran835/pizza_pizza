from tkinter import *
from tkinter import messagebox as mb

from Pizza import Pizza

def is_valid_size(size):
    sizes = ['small', 'medium', 'large']
    return size.lower() in sizes
    
    
def add_toppings(pizza):
    if pepperoni.get() == 1:
        pizza.add_topping("Pepperoni")
    if sausage.get() == 1:
        pizza.add_topping("Sausage")
    if onion.get() == 1:
        pizza.add_topping("Onion")
    if mushroom.get() == 1:
        pizza.add_topping("Mushroom")

def add_crust(pizza):
    CRUST_VALUES = {
        0: "Standard",
        1: "Thin-crust",
        2: "Deep-dish",
        3: "Hand-tossed"
    }

    crust_type = CRUST_VALUES[crust_var.get()]
    
    pizza.set_crust_type(crust_type)

def calculate_pizza_cost():
    TAX_PERCENTAGE = 0.0875

    pizza_size = size_entry.get().lower()
    if is_valid_size(pizza_size) is False:
        mb.showerror(title="Size Error", message='Please enter a valid size: small, medium, large.')
        return None
    
    PIZZA_PRICES = {
        'small': 10.99,
        'medium': 12.99,
        'large': 14.99
    }
    
    pizza_price = PIZZA_PRICES[pizza_size]
    if pizza_price is None:
        mb.showerror(title="Size Error", message='Price for pizza size not found.')
        return None
    
    pizza = Pizza(pizza_size, crust_var.get(), pizza_price)

    add_toppings(pizza)
    add_crust(pizza)
        
    total_pizza_price = pizza.get_total_price()
    total_cost = total_pizza_price + (total_pizza_price * TAX_PERCENTAGE)

    return [total_cost, total_pizza_price, pizza]
    

def print_toppings(pizza):
    toppings = pizza.get_toppings()
    output.insert(END, "Toppings: ")
    output.insert(END, "Cheese ")
    
    if len(toppings) == 0:
        return
    
    for topping in toppings:
        output.insert(END, topping + " ")
    output.insert(END, "\n")

def print_crust_type(pizza):
    crust_type = pizza.get_crust_type()
    output.insert(END, "Crust type: " + crust_type + "\n")

def submit_order():
    pizza_order_size = size_entry.get()
    pizza_order = calculate_pizza_cost()
    
    if pizza_order is None:
        return
    
    tax, final_cost, pizza = pizza_order
    
    output.insert(END, "Your Receipt...\n")
    output.insert(END, "Your order: " + pizza_order_size + "\n")
    print_crust_type(pizza)
    print_toppings(pizza)
    
    output.insert(END, "\n")
    
    output.insert(END, f"Tax: ${tax:.2f}\n")
    output.insert(END, f"Your final cost is ${final_cost:.2f}.")


window = Tk()
window.title("Richie's Pizzeria")
window.geometry("1200x900")
window.configure(background="white")

photo = PhotoImage(file="pizza_header1.gif")
image_label = Label(window, image=photo)
image_label.pack()

# Adds label
name_label = Label(window, text="Enter your pizza size:", bg= "yellow", fg="black", font="arial 16 bold")
name_label.pack()

# Adds textfield
size_entry = Entry(window, width=15, bg="white", bd= 2, font="arial 16 bold", )
size_entry.pack()

# Adds label
crust_label = Label(window, text="Select crust:", bg="yellow", fg="black", font="arial 16 bold")
crust_label.pack()

# Adds radio button
crust_var = IntVar()
radio1 = Radiobutton(window, text="Thin-crust", variable=crust_var, value=1)
radio2 = Radiobutton(window, text="Deep-dish", variable=crust_var, value=2)
radio3 = Radiobutton(window, text="Hand-tossed", variable=crust_var, value=3)
radio1.pack()
radio2.pack()
radio3.pack()

# Adds Label
topping_label = Label(window, text="Select toppings:", bg="yellow", fg="black", font="arial 16 bold")
topping_label.pack()

# Adds check button
pepperoni = IntVar()
sausage= IntVar()
onion = IntVar()
mushroom = IntVar()

Check1 = Checkbutton(window, text = "Pepperoni", variable = pepperoni, onvalue = 1, width = 15)
Check2 = Checkbutton(window, text = "Sausage", variable = sausage, onvalue = 1, width = 15)
Check3 = Checkbutton(window, text = "Onion", variable = onion, onvalue = 1, width = 15)
Check4 = Checkbutton(window, text = "Mushroom", variable = mushroom, onvalue = 1, width = 15)

Check1.pack()
Check2.pack()
Check3.pack()
Check4.pack()

# Adds button
submit_button = Button(window, text="Submit your order:", width = 30, command=submit_order)
submit_button.pack()

output = Text(window, width=30, height=8, wrap=WORD, background="white")
output.pack()

window.mainloop()