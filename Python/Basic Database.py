from tkinter import *
#from PIL import ImageTk, Image
import sqlite3
from tkinter import messagebox
root = Tk()
root.title("Database")


# Create or connect to a DATABASE
conn = sqlite3.connect('address_book.db')

# Create CURSOR
c = conn.cursor()

# Commented out the Table to not recreate it every time the program is ran
'''
# Create TABLES
c.execute("""CREATE TABLE addresses (
  first_name text, 
  last_name text, 
  address text, 
  city text, 
  state text,
  zipcode integer
)
""")
'''

def update():
  conn = sqlite3.connect('address_book.db')
  c = conn.cursor()

  record_id = delete_box.get()
  # Updating
  c.execute("""UPDATE addresses SET 
    first_name = :first, 
    last_name = :last, 
    address = :address, 
    city = :city, 
    state = :state,
    zipcode = :zipcode

    WHERE oid = :oid""",
    {
      'first': f_name_e.get(), 
      'last': l_name_e.get(),
      'address': address_e.get(),
      'city': city_e.get(),
      'state': state_e.get(),
      'zipcode': zipcode_e.get(),
      'oid': record_id
    })
  conn.commit()
  conn.close()
  editor.destroy()

# Create 'edit' function to update record
def edit():
  conn = sqlite3.connect('address_book.db')
  c = conn.cursor()
  try:
    # Grabs all the data from the selected oid
    c.execute("SELECT * FROM addresses WHERE oid= " + delete_box.get())
    records = c.fetchall()
    global editor
    editor = Tk()
    editor.title("Database/Editor")

    
    global f_name_e
    global l_name_e
    global address_e
    global city_e
    global state_e
    global zipcode_e

    # Create text boxes
    f_name_e = Entry(editor, width=30)
    l_name_e = Entry(editor, width=30)
    address_e = Entry(editor, width=30)
    city_e = Entry(editor, width=30)
    state_e = Entry(editor, width=30)
    zipcode_e = Entry(editor, width=30)

    f_name_e.grid(row=0, column= 1, padx=20, pady=(10, 0))
    l_name_e.grid(row=1, column= 1, padx=20)
    address_e.grid(row=2, column= 1, padx=20)
    city_e.grid(row=3, column= 1, padx=20)
    state_e.grid(row=4, column= 1, padx=20)
    zipcode_e.grid(row=5, column=1, padx=20)

    # Create text box labels
    Label(editor, text="First Name:").grid(row=0, column=0, pady=(10, 0))
    Label(editor, text="Last Name:").grid(row=1, column=0)
    Label(editor, text="Address:").grid(row=2, column=0)
    Label(editor, text="City:").grid(row=3, column=0)
    Label(editor, text="State:").grid(row=4, column=0)
    Label(editor, text="Zipcode:").grid(row=5, column=0)

    

    # Create 'save' button
    save_btn = Button(editor, text="Save Record", command=update)
    save_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

    for record in records:
      f_name_e.insert(0, record[0])
      l_name_e.insert(0, record[1])
      address_e.insert(0, record[2])
      city_e.insert(0, record[3])
      state_e.insert(0, record[4])
      zipcode_e.insert(0, record[5])

    conn.commit()
    conn.close()
  except sqlite3.OperationalError:
    messagebox.showwarning("Operational Error", "Please Enter an ID")

# Create 'delete' function
def delete():
  conn = sqlite3.connect('address_book.db')
  c = conn.cursor()
  try:
    # Delete
    c.execute("DELETE from addresses WHERE oid= " + delete_box.get())
    delete_box.delete(0, END)
    conn.commit()
    conn.close()
  except sqlite3.OperationalError:
    messagebox.showwarning("Operational Error", "Please Enter an ID") 

# Create submit function
def submit():
  conn = sqlite3.connect('address_book.db')
  c = conn.cursor()

  # Insert into Table
  c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
    {
      'f_name': f_name.get(),
      'l_name': l_name.get(),
      'address': address.get(),
      'city': city.get(),
      'state': state.get(),
      'zipcode': zipcode.get()
    })
  conn.commit()
  conn.close()

  f_name.delete(0, END)
  l_name.delete(0, END)
  address.delete(0, END)
  city.delete(0, END)
  state.delete(0, END)
  zipcode.delete(0, END)

# Create 'query' fubction
def query():
  conn = sqlite3.connect('address_book.db')
  c = conn.cursor()

  # Selects 'everything' and its unique id from the 'addresses' table
  c.execute("SELECT *, oid FROM addresses")
  records = c.fetchall()

  # Prints items in each tuple
  print_records = ''
  for x in records:
    print_records += str(x) + "\n"

  
  query_label = Label(root, text=print_records)
  query_label.grid(row=12, column=0, columnspan=2)

  conn.commit()
  conn.close()

# Create text boxes
f_name = Entry(root, width=30)
l_name = Entry(root, width=30)
address = Entry(root, width=30)
city = Entry(root, width=30)
state = Entry(root, width=30)
zipcode = Entry(root, width=30)

f_name.grid(row=0, column= 1, padx=20, pady=(10, 0))
l_name.grid(row=1, column= 1, padx=20)
address.grid(row=2, column= 1, padx=20)
city.grid(row=3, column= 1, padx=20)
state.grid(row=4, column= 1, padx=20)
zipcode.grid(row=5, column=1, padx=20)

delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1)

# Create text box labels
Label(root, text="First Name:").grid(row=0, column=0, pady=(10, 0))
Label(root, text="Last Name:").grid(row=1, column=0)
Label(root, text="Address:").grid(row=2, column=0)
Label(root, text="City:").grid(row=3, column=0)
Label(root, text="State:").grid(row=4, column=0)
Label(root, text="Zipcode:").grid(row=5, column=0)
Label(root, text="Select ID:").grid(row=9, column=0)
# Create 'submit' button
submit_btn = Button(root, text="Add Record To Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create 'query' button
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=128)

# Create delete button
delete_btn = Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=130)

# Create an update button
edit_btn = Button(root, text="Edit Record", command=edit)
edit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

# Commit changes
conn.commit()

# Close connection
conn.close()

mainloop()