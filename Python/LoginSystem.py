from tkinter import *
import sqlite3
#from PIL import ImageTk, Image
from tkinter import messagebox
root = Tk()
root.title("Login System")
root.geometry("320x250")

conn = sqlite3.connect('user.db')
c = conn.cursor()

'''
c.execute("""CREATE TABLE users (
  username text,
  screen_name text,
  password text
)
""")
'''

def new_user():
  new = Tk()
  new.title("Login System-New User")

  def create():
    conn = sqlite3.connect('user.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    records = c.fetchall()
    
    for x in range(len(records)):
      if u_name2.get() != records[x][0]:
        c.execute("INSERT INTO users VALUES (:u_name, :scr_name, :p_word)",
        {
          'u_name': u_name2.get(),
          'scr_name': scr_name.get(),
          'p_word': p_word2.get()
        })
        
        conn.commit()
        conn.close()
        new.destroy()
      else:
        messagebox.askokcancel("Username Taken", "Username taken, please Enter a unique username") 
        

  scr_name = Entry(new, width=30)
  u_name2 = Entry(new, width=30)
  p_word2 = Entry(new, width=30)

  u_name2.insert(0, u_name.get())
  p_word2.insert(0, p_word.get())
  create_btn = Button(new, text="Join", command=create)

  scr_name.grid(row=1, column=1, columnspan=2, pady=(10, 0), padx=10)
  u_name2.grid(row=2, column=1, columnspan=2)
  p_word2.grid(row=3, column=1, columnspan=2)
  create_btn.grid(row=4, column=1, columnspan=2)
  

  Label(new, text="Name:").grid(row=1, column=0, pady=(10,0))
  Label(new, text="Username:").grid(row=2, column=0, pady=(10, 0))
  Label(new, text="Password:").grid(row=3, column=0)

def show():
  conn = sqlite3.connect('user.db')
  c = conn.cursor()

  c.execute("SELECT *, oid FROM users")
  records = c.fetchall()

  # Prints items in each tuple
  print_records = ''
  for x in records:
    print_records += str(x) + "\n"

    query_label = Label(admin, text=print_records)
    query_label.grid(row=3, column=1)
  conn.commit()
  conn.close()

def delete():
  conn = sqlite3.connect('user.db')
  c = conn.cursor()
  try:
    # Delete
    c.execute("DELETE from users WHERE oid= " + id_sel.get())
    id_sel.delete(0, END)
    conn.commit()
    conn.close()
  except sqlite3.OperationalError:
    messagebox.showwarning("Operational Error", "Please Enter an ID") 

def admin():
  global admin
  global id_sel
  admin = Tk()
  admin.title("Admin")
  id_sel = Entry(admin, width=30)
  id_sel.grid(row=0, column=1)
  Label(admin, text="Type ID:").grid(row=0, column=0)
  Button(admin, text="Show Users", command=show).grid(row=2, column=0)
  Button(admin, text="Delete User", command=delete).grid(row=1, column=0)

def login():
  conn = sqlite3.connect('user.db')
  c = conn.cursor()
  c.execute("SELECT * FROM users")
  records = c.fetchall()
  
  for usr in range(len(records)):
    if u_name.get() == records[usr][0]:
      x = 1
      
      if p_word.get() == records[usr][2]:
        web = Tk()
        web.title("SITE")
        root.destroy()
        break
      else:
        messagebox.askokcancel("Invalid Password", "Please Enter a valid password") 
        break
    else:
      x = 0
      
  # This has to be outside the for loop
  if x == 0:
    messagebox.askokcancel("Invalid Username", "Please Enter a valid username") 

  conn.commit()
  conn.close()

#my_img = ImageTk.PhotoImage(Image.open("C:/Users/kingc/Pictures/download.jpg"))
#Label(image=my_img).grid(row=0, column=1, columnspan=2)
# Text Boxes
u_name = Entry(root, width=30)
p_word = Entry(root, width=30)
# Display
u_name.grid(row=1, column=1, columnspan=2, pady=(10, 0), padx=10)
p_word.grid(row=2, column=1, columnspan=2)
# Labels
Label(root, text="Username:").grid(row=1, column=0, pady=(10, 0))
Label(root, text="Password:").grid(row=2, column=0)
# Buttons
login_btn = Button(root, text="Sign In", command=login)
new_user_btn = Button(root, text="Create New Account", command=new_user)
admin_btn = Button(root, text="Admin", command=admin)

login_btn.grid(row=3, column=1)
new_user_btn.grid(row=3, column=2)
admin_btn.grid(row=4, column=2)


conn.commit()
conn.close()
mainloop()