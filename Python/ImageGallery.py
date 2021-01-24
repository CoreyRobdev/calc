from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title('Image Gallery')

# Grabs an image from file
my_img0 = ImageTk.PhotoImage(Image.open("C:/Users/kingc/Pictures/Google Earth VR/Monticello.jpg"))
my_img1 = ImageTk.PhotoImage(Image.open("C:/Users/kingc/Pictures/900.PNG"))
my_img2 = ImageTk.PhotoImage(Image.open("C:/Users/kingc/Pictures/Capture.PNG"))
my_img3 = ImageTk.PhotoImage(Image.open("C:/Users/kingc/Pictures/Screenshots/Screenshot (1).png"))
my_img4 = ImageTk.PhotoImage(Image.open("C:/Users/kingc/Pictures/Feedback/bob/Capture001.png"))

num = 0
image_list = [my_img0, my_img1, my_img2, my_img3, my_img4]

status = Label(root, text="Images " + str(num+1) + " of " + str(len(image_list)), bd=1, relief=SUNKEN)

my_label = Label(image=my_img0)
my_label.grid(row=2, column=0, columnspan=3)


def forward():
  global my_label
  global num
  global status
  num += 1
  
  if num < 0:
    status = Label(root, text="Images " + str(num+1+len(image_list)) + " of " + str(len(image_list)), bd=1, relief=SUNKEN)
  else:
    status = Label(root, text="Images " + str(num+1) + " of " + str(len(image_list)), bd=1, relief=SUNKEN)
    
  my_label.grid_forget()
  try:
    my_label = Label(image=image_list[num])
  except IndexError:
    my_label = Label(image=my_img0)
    num = 0
    status = Label(root, text="Images " + str(num+1) + " of " + str(len(image_list)), bd=1, relief=SUNKEN)
    
  status.grid(row=0, column=0, columnspan=3, sticky=W+E)
  my_label.grid(row=2, column=0, columnspan=3)
  
def back():
  global my_label
  global num
  global status
  num -= 1

  if num < 0:
    status = Label(root, text="Images " + str(num+1+len(image_list)) + " of " + str(len(image_list)), bd=1, relief=SUNKEN)
  else:
    status = Label(root, text="Images " + str(num+1) + " of " + str(len(image_list)), bd=1, relief=SUNKEN)
  my_label.grid_forget()
  try:
    my_label = Label(image=image_list[num])
  except IndexError:
    my_label = Label(image=my_img4)
    num = -1
    status = Label(root, text="Images " + str(num+1) + " of " + str(len(image_list)), bd=1, relief=SUNKEN)

  status.grid(row=0, column=0, columnspan=3, sticky=W+E)
  my_label.grid(row=2, column=0, columnspan=3)
  
button_back = Button(root, text="<<<", command=back)
button_quit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>>", command=forward)

button_back.grid(row=1, column=0, columnspan=1)
button_forward.grid(row=1, column=2, columnspan=1)
button_quit.grid(row=1, column=1, columnspan=1)
# Spans from WEST to EAST
status.grid(row=0, column=0, columnspan=3, sticky=W+E)

root.mainloop()