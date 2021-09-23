from tkinter import *

root = Tk(className=" HOTEL MANAGEMENT")
root.geometry('1925x1070')


# heading
heading_label = Label(root,text="---------  DEVELOPERS  ---------",font=('Orbitron',15),bg="black",fg="white")
heading_label.pack(fill=X)


# image1
image1= PhotoImage(file = "images/shivika.png")
image1 = image1.zoom(40)
image1 = image1.subsample(32)
label_for_image1 = Label(root, image=image1)
label_for_image1.pack(side=LEFT)

# image2
image2= PhotoImage(file = "images/vidushi.png")
image2 = image2.zoom(40)
image2 = image2.subsample(32)
label_for_image2 = Label(root, image=image2)
label_for_image2.pack(side=RIGHT)

# image3
image3= PhotoImage(file = "images/vaibhav.png")
image3 = image3.zoom(40)
image3 = image3.subsample(32)
label_for_image3 = Label(root, image=image3)
label_for_image3.pack(side=TOP , pady=170)

# NAME LABELS
s_label=Label(root,text="Shivika Gupta",font=('Times New Roman',25,'bold'))
c_label=Label(root,text="Vidushi Chaturvedi",font=('Times New Roman',25,'bold'))
v_label=Label(root,text="Vaibhav Billore",font=('Times New Roman',25,'bold'))

s_label.place(relx=0.041,rely=0.165)
c_label.place(relx=0.75,rely=0.165)
v_label.place(relx=0.42,rely=0.165)

root.mainloop()