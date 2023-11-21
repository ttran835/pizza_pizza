from tkinter import *

def click():
    pizza_order = textEntry.get()
    if total_cost() == "no choices":
        output.insert(END, "Please enter a valid response by reloading the page.")
        textEntry.delete(0, END)
    else:
        output.insert(END, "Your Receipt...\n")
        output.insert(END, "Your order: " + pizza_order + "\n")

        crust_type = "Standard"

        if crust_var.get() == 1:
            crust_type = "Thin-crust"
        elif crust_var.get() == 2:
            crust_type = "Deep-dish"
        elif crust_var.get() == 3:
            crust_type = "Hand-tossed"
        output.insert(END, "Crust type: " + crust_type + "\n")

        output.insert(END, "Toppings: ")
        output.insert(END, "Cheese ")
        if pepperoni.get() == 1:
            output.insert(END, "Pepperoni ")
        if sausage.get() == 1:
            output.insert(END, "Sausage ")
        if onion.get() == 1:
            output.insert(END, "Onion ")
        if mushroom.get() == 1:
            output.insert(END, "Mushroom ")
        
        output.insert(END, "\n")
        output.insert(END, f"Tax: ${total_cost()[0]:.2f}\n")
        output.insert(END, f"Your final cost is ${total_cost()[1]:.2f}.")


def total_cost():
    cost = 0
    toppings = 0
    TAX_PERCENTAGE = 0.0875

    if textEntry.get().lower() == "small":
        cost = 10.99
    elif textEntry.get().lower() == "medium":
        cost = 12.99
    elif textEntry.get().lower() == "large":
        cost = 14.99
    else:
        return "no choices"


    if pepperoni.get() == 1:
        cost += 1.25
    if sausage.get() == 1:
        cost += 1.25
    if onion.get() == 1:
        cost += 1.25
    if mushroom.get() == 1:
        cost += 1.25

    cost = cost + (cost * TAX_PERCENTAGE)

    return [cost * TAX_PERCENTAGE, cost]
    




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
textEntry = Entry(window, width=15, bg="white", bd= 2, font="arial 16 bold", )
textEntry.pack()

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
submit_button = Button(window, text="Submit your order:", width = 30, command=click)
submit_button.pack()

output = Text(window, width=30, height=8, wrap=WORD, background="white")
output.pack()


window.mainloop()