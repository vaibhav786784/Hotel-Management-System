from tkinter import *
import mysql.connector

root = Tk(className=" HOTEL MANAGEMENT")
root.geometry('1920x600')

# heading
heading_label = Label(root, text="---------  ALL CUSTOMERS  ---------", font=('Orbitron', 15), bg="black", fg="white")
heading_label.pack(fill=X)

top_frame = Frame(root)
top_frame.pack()

# customer text view
text = Text(root, bd=5, bg="white", fg='black', width=200, font=('Times New Roman', 13))
text.place(rely=0.1)

# database
mydb = mysql.connector.connect(host='localhost', user='root', password='vabhu886vabhu@', database='hotel')
cur = mydb.cursor()
cur.execute('SELECT * from hotel_management')
result = cur.fetchall()
title = "First Name\t Last Name\t Phone Number\t Email id\t\t\t\t\t Address\t\t\t\t\t Room No\t\t Room Type\t\t " \
        "People\t " \
        "Days\n"
text.insert(INSERT, title)
formatting = "-------------------------------------------------------------------------------------------" \
             "-------------------------------------------------------------------------------------------" \
             "------------------------------------------------------------------------------------------\n"
text.insert(INSERT, formatting)
text.insert(INSERT, formatting)
for i in result:
    a = list(i)
    rt = ''
    if a[6] == 1:
        rt = "AC"
    else:
        rt = "Non-AC"
    s = a[0] + "\t" + "   " + a[1] + "\t" + "   " + str(a[2]) + "\t" + "   "+ a[3] + "\t\t\t" + "   " + a[4] + "\t\t\t\t\t\t\t" + "      "+ \
        str(a[5]) + "\t\t" +"   "+ rt + "\t\t " + str(a[7]) + " \t" + str(a[8]) + "\n\n"
    text.insert(INSERT, s)

root.mainloop()
