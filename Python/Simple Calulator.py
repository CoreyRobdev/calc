from tkinter import *
root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth=5)

# 'Columnspan' stretches the Entry field across 3 columns
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)



def buttonAdd(num):
 
  # Grabs and saves whats currently in the window
  current = e.get()
  # Deletes it in the window
  e.delete(0, END)
  # Displays the number pressed appended to the old number
  e.insert(0, str(current) + str(num))

ans = 0
def button_clear():
  global ans
  ans = 0 
  e.delete(0, END)

# -
def button_min():
  global ans
  global math
  math = "-"
  ans = float(e.get())
  e.delete(0, END)

# *
def button_tim():
  global ans
  global math
  math = "*"
  ans = float(e.get())
  e.delete(0, END)

# /
def button_split():
  global ans
  global math
  math = "/"
  ans = float(e.get())
  e.delete(0, END)

# +
def button_plus():
  global ans
  global math 
  math = "+"
  ans = float(e.get())
  e.delete(0, END)
# =
def button_equals():
  global ans
  global math
  new = float(e.get())
  if math == "+":
    ans = ans + new
  elif math == "-":
    ans = ans - new
  elif math == "*":
    ans = ans * new
  elif math == "/":
    ans = ans / new

  e.delete(0, END)
  e.insert(0, str(ans))
  ans = 0
# Define buttons
# 'lambda' allows you to pass arguments through the function in the button
button1 = Button(root, text="1", padx=40, pady=20, command=lambda: buttonAdd(1))
button2 = Button(root, text="2", padx=40, pady=20, command=lambda: buttonAdd(2))
button3 = Button(root, text="3", padx=40, pady=20, command=lambda: buttonAdd(3))
button4 = Button(root, text="4", padx=40, pady=20, command=lambda: buttonAdd(4))
button5 = Button(root, text="5", padx=40, pady=20, command=lambda: buttonAdd(5))
button6 = Button(root, text="6", padx=40, pady=20, command=lambda: buttonAdd(6))
button7 = Button(root, text="7", padx=40, pady=20, command=lambda: buttonAdd(7))
button8 = Button(root, text="8", padx=40, pady=20, command=lambda: buttonAdd(8))
button9 = Button(root, text="9", padx=40, pady=20, command=lambda: buttonAdd(9))
button0 = Button(root, text="0", padx=40, pady=20, command=lambda: buttonAdd(0))

button_add = Button(root, text="+", padx=39, pady=20, command=button_plus)
button_sub = Button(root, text="-", padx=40, pady=20, command=button_min)
button_mul = Button(root, text="*", padx=41, pady=20, command=button_tim)
button_div = Button(root, text="/", padx=41, pady=20, command=button_split)
buttonEqual = Button(root, text="=", padx=88, pady=20, command=button_equals)
buttonClear = Button(root, text="Clear", padx=78, pady=20, command=button_clear)

# Displaying buttons
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0)

button_add.grid(row=5, column=0)
buttonEqual.grid(row=5, column=1, columnspan=2)
buttonClear.grid(row=4, column=1, columnspan=2)

button_sub.grid(row=6, column=0)
button_mul.grid(row=6, column=1)
button_div.grid(row=6, column=2)

root.mainloop()
