# Importing Libraries for GUI
import tkinter as tk
from tkinter import ttk, messagebox

# Importing Database Driver
import sqlite3

# Importing SMTP for Email sending
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# Creating Email Template
msg= MIMEMultipart()
msg["From"]= "demo.internship@gmail.com"
password= "demo123@"

# creating window
root = tk.Tk()
root.title("Entry Management System")

# connecting with Database
connection = sqlite3.connect('management_system.db', timeout=10)

# Creating Visitors Table SCHEMA
TABLE_NAME_VISITORS = "Visitors"
VISITORS_ID = "visitors_id"
VISITORS_NAME = "visitors_name"
VISITORS_EMAIL = "visitors_email"
VISITORS_PHONE = "visitors_phone"
VISITORS_CHECKIN = "visitors_checkin"
VISITORS_CHECKOUT = "visitors_checkout"

# Creating Hosts Table SCHEMA
TABLE_NAME_HOSTS = "Hosts"
HOSTS_ID = "hosts_id"
HOSTS_NAME = "hosts_name"
HOSTS_EMAIL = "hosts_email"
HOSTS_PHONE = "hosts_phone"

# Creating Tables (If not exist)
connection.execute(" CREATE TABLE IF NOT EXISTS " + TABLE_NAME_VISITORS + " ( " + VISITORS_ID +
                   " INTEGER PRIMARY KEY AUTOINCREMENT, " +
                   VISITORS_NAME + " TEXT, " + VISITORS_EMAIL + " TEXT, " +
                   VISITORS_PHONE + " INTEGER, " + VISITORS_CHECKIN + " TEXT, " + VISITORS_CHECKOUT + " TEXT);")

connection.execute(" CREATE TABLE IF NOT EXISTS " + TABLE_NAME_HOSTS + " ( " + HOSTS_ID +
                   " INTEGER PRIMARY KEY AUTOINCREMENT, " +
                   HOSTS_NAME + " TEXT, " + HOSTS_EMAIL + " TEXT, " +
                   HOSTS_PHONE + " INTEGER);")


appLabel = tk.Label(root, text="Entry Management System", fg="#06a099", width=35)
appLabel.config(font=("Sylfaen", 30))
appLabel.grid(row=0, columnspan=2, padx=(10,10), pady=(30, 0))

class Visitor:
    VisitorName = ""
    Email = ""
    phoneNumber = 0
    checkin = ""
    checkout = ""
    HostName = ""
    HostEmail = ""
    HostPhone = 0

    def __init__(self, VisitorName,Email,phoneNumber,checkin,checkout,HostName,HostEmail,HostPhone):
        self.VisitorName = VisitorName
        self.Email = Email
        self.phoneNumber = phoneNumber
        self.checkin = checkin
        self.checkout = checkout
        self.HostName = HostName
        self.HostEmail = HostEmail
        self.HostPhone = HostPhone

# Creating Labels of GUI
nameLabel = tk.Label(root, text="Enter your name", width=40, anchor='w',
                     font=("Sylfaen", 12)).grid(row=1, column=0, padx=(10,0),
                                                pady=(30, 0))
emailLabel = tk.Label(root, text="Enter your Email", width=40, anchor='w',
                        font=("Sylfaen", 12)).grid(row=2, column=0, padx=(10,0))
phoneLabel = tk.Label(root, text="Enter your phone number", width=40, anchor='w',
                      font=("Sylfaen", 12)).grid(row=3, column=0, padx=(10,0))
checkinLabel = tk.Label(root, text="Enter your CheckIn Time", width=40, anchor='w',
                        font=("Sylfaen", 12)).grid(row=4, column=0, padx=(10,0))
checkoutLabel = tk.Label(root, text="Enter your CheckOut Time", width=40, anchor='w',
                        font=("Sylfaen", 12)).grid(row=5, column=0, padx=(10,0))
HostNameLabel = tk.Label(root, text="Enter Host Name", width=40, anchor='w',
                        font=("Sylfaen", 12)).grid(row=6, column=0, padx=(10,0))
HostEmailLabel = tk.Label(root, text="Enter Host Email", width=40, anchor='w',
                        font=("Sylfaen", 12)).grid(row=7, column=0, padx=(10,0))
HostPhoneLabel = tk.Label(root, text="Enter Host Phone Number", width=40, anchor='w',
                        font=("Sylfaen", 12)).grid(row=8, column=0, padx=(10,0))

# Enetring Data into GUI
nameEntry = tk.Entry(root, width = 30)
emailEntry = tk.Entry(root, width = 30)
phoneEntry = tk.Entry(root, width = 30)
checkinEntry = tk.Entry(root, width = 30)
checkoutEntry = tk.Entry(root, width = 30)
HostNameEntry = tk.Entry(root, width = 30)
HostEmailEntry = tk.Entry(root, width = 30)
HostPhoneEntry = tk.Entry(root, width = 30)

nameEntry.grid(row=1, column=1, padx=(0,10), pady=(30, 20))
emailEntry.grid(row=2, column=1, padx=(0,10), pady = 20)
phoneEntry.grid(row=3, column=1, padx=(0,10), pady = 20)
checkinEntry.grid(row=4, column=1, padx=(0,10), pady = 20)
checkoutEntry.grid(row=5, column=1, padx=(0,10), pady = 20)
HostNameEntry.grid(row=6, column=1, padx=(0,10), pady = 20)
HostEmailEntry.grid(row=7, column=1, padx=(0,10), pady = 20)
HostPhoneEntry.grid(row=8, column=1, padx=(0,10), pady = 20)

# Taking Input from the user 
def takeNameInput():
    global nameEntry, emailEntry, phoneEntry, checkinEntry, checkoutEntry
    global list
    global TABLE_NAME, VISITORS_NAME, VISITORS_EMAIL, VISITORS_PHONE, VISITORS_CHECKIN, VISITORS_CHECKOUT
    username = nameEntry.get()
    nameEntry.delete(0, tk.END)
    email = emailEntry.get()
    emailEntry.delete(0, tk.END)
    phone = int(phoneEntry.get())
    phoneEntry.delete(0, tk.END)
    checkin = checkinEntry.get()
    checkinEntry.delete(0, tk.END)
    checkout = checkoutEntry.get()
    checkoutEntry.delete(0, tk.END)
    hostname = HostNameEntry.get()
    HostNameEntry.delete(0, tk.END)
    hostemail = HostEmailEntry.get()
    HostEmailEntry.delete(0, tk.END)
    hostphone = HostPhoneEntry.get()
    HostPhoneEntry.delete(0, tk.END)
    
    # Inserting Data into Tables
    connection.execute("INSERT INTO " + TABLE_NAME_VISITORS + " ( " + VISITORS_NAME + ", " +
                       VISITORS_EMAIL + ", " + VISITORS_PHONE + ", " +
                       VISITORS_CHECKIN + ", " + VISITORS_CHECKOUT + " ) VALUES ( '"
                       + username + "', '" + email + "', '" + str(phone) + "', '" + checkin + "', '" + checkout + "' ); ")
    
    connection.execute("INSERT INTO " + TABLE_NAME_HOSTS + " ( " + HOSTS_NAME + ", " +
                       HOSTS_EMAIL + ", " + HOSTS_PHONE + " ) VALUES ( '"
                       + hostname + "', '" + hostemail + "', '" + str(hostphone) + "' ); ")
    
    connection.commit()
    
    # Sending mail to Host about Visitor
    msg["To"]= hostemail
    msg["Subject"]= "Visitor's Details"
    body="<p>Name : %s</p><br><p>Email : %s</p><br><p>Phone : %s</p><br><p>CheckIn time : %s</p><br><p>CheckOut time : %s</p>" %(username,email,phone,checkin,checkout)
    msg.attach(MIMEText(body,'html'))
    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    smtpserver.login(msg["From"],password)    
    smtpserver.sendmail(msg["From"],msg["To"],msg.as_string())
    
    cursor = connection.cursor()
    
    # checkOut time is equal to current time ???
    cur = cursor.execute("SELECT * FROM " + TABLE_NAME_VISITORS + " WHERE (SELECT strftime('%H:%M',datetime(CURRENT_TIMESTAMP, 'localtime'))) = (SELECT substr(trim( " + VISITORS_CHECKOUT + "),1,instr(trim( "+ VISITORS_CHECKOUT + ")||' ',' ')-1) FROM " + TABLE_NAME_VISITORS + ") ;")
    result= cur.fetchall()
    
    # sending email at checkout time to Visitor
    if len(result) > 0:    
        msg["To"]= email
        msg["Subject"]= "Entry Details"
        body="<p>Name : %s</p><br><p>Phone : %s</p><br><p>CheckIn time : %s</p><br><p>CheckOut time : %s</p><br><p>Host Name : %s</p><br><p>Address : %s</p>" %(result[0][1],result[0][3],result[0][4],result[0][5],hostname,"ABCD")
        msg.attach(MIMEText(body,'html'))
        smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo()
        smtpserver.login(msg["From"],password)    
        smtpserver.sendmail(msg["From"],msg["To"],msg.as_string())
        smtpserver.quit()
        
    # Showing Message Box    
    messagebox.showinfo("Success", "Data Saved Successfully.")
        
        
    
# Displaying Visitor table
def destroyRootWindow():
    root.destroy()
    secondWindow = tk.Tk()

    secondWindow.title("Display results")

    appLabel = tk.Label(secondWindow, text="Entry Management System",
                        fg="#06a099", width=40)
    appLabel.config(font=("Sylfaen", 30))
    appLabel.pack()

    tree = ttk.Treeview(secondWindow)
    tree["columns"] = ("one", "two", "three", "four","five")

    tree.heading("one", text="Visitor Name")
    tree.heading("two", text="Email")
    tree.heading("three", text="Phone Number")
    tree.heading("four", text="CheckIn Time")
    tree.heading("five", text="CheckOut Time")

    cursor = connection.execute("SELECT * FROM " + TABLE_NAME_VISITORS + " ;")
    i = 0

    for row in cursor:
        tree.insert('', i, text="Visitor " + str(row[0]),
                    values=(row[1], row[2],
                            row[3], row[4], row[5]))
        i = i + 1 

    tree.pack()
    secondWindow.mainloop()

# Displaying Host table
def destroyRootWindow2():
    root.destroy()
    thirdWindow = tk.Tk()

    thirdWindow.title("Display results")

    appLabel = tk.Label(thirdWindow, text="Entry Management System",
                        fg="#06a099", width=40)
    appLabel.config(font=("Sylfaen", 30))
    appLabel.pack()

    tree = ttk.Treeview(thirdWindow)
    tree["columns"] = ("one", "two", "three")

    tree.heading("one", text="Visitor Name")
    tree.heading("two", text="Email")
    tree.heading("three", text="Phone Number")

    cursor = connection.execute("SELECT * FROM " + TABLE_NAME_HOSTS + " ;")
    i = 0

    for row in cursor:
        tree.insert('', i, text="Host " + str(row[0]),
                    values=(row[1], row[2], row[3]))
        i = i + 1 

    tree.pack()
    thirdWindow.mainloop()

# Creating Buttons
button = tk.Button(root, text="Take input", command=lambda :takeNameInput())
button.grid(row=9, column=0, pady=30)

displayButton = tk.Button(root, text="Display Visitors", command=lambda :destroyRootWindow())
displayButton.grid(row=9, column=1)

displayButton2 = tk.Button(root, text="Display Hosts", command=lambda :destroyRootWindow2())
displayButton2.grid(row=10, column=1)

root.mainloop()
