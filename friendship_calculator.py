# Python Tkinter GUI based "FRIENDSHIP CALCULATOR"
# import tkinter
from tkinter import *
# import random module
import random
# Creating GUI window
root = Tk()
# Defining the container size, width=500, height=380
root.geometry('500x380')
# Title of the container
root.title('Friendship Calculator by anish')

# Function to calculate friendship percentage
# between the user and partner

def calculate_friendship():
	# value will contain digits between 0-9
	st = '0123456789'
	# result will be in double digits
	digit = 2
	temp = "".join(random.sample(st, digit))
	result.config(text=temp)


# Heading on Top
heading = Label(root, text='Friend Calculator - How much is he/she into you')
heading.pack()

# Slot/input for the first name
slot1 = Label(root, text="Enter Your Name:")
slot1.pack()
name1 = Entry(root)
name1.pack()

# Slot/input for the partner name
slot2 = Label(root, text="Enter Your Friend Name:")
slot2.pack()
name2 = Entry(root)
name2.pack()

bt = Button(root, text="Calculate", height=1,
			width=7, command=calculate_friendship)
bt.pack()

# Text on result slot
result = Label(root, text='Friendship Percentage between both of You: ')
result.pack()

# Starting the GUI
root.mainloop()