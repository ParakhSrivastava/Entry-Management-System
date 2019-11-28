# Entry-Management-System
> Keeping the records of visitors that we have in office and outside, with the help of an application - *ENTRY MANAGEMENT SYSTEM*

## Looks-Like
![](https://github.com/ParakhSrivastava/Entry-Management-System/blob/master/EMS.PNG)
![](https://github.com/ParakhSrivastava/Entry-Management-System/blob/master/EMS_Database.PNG)

## Skills Used 
* Python
* SQLite Driver (for Database)
* Tkinter (GUI framework)
* SMTP Protocol

## Steps Involved
* Importing Libraries 
* Creating GUI Window
* Connecting Database (SQLite)
* Creating Tables
* Creating UI
* Data Input
* Sending E-Mails
* Displaying Records(Data)
* Creating Buttons 

## Description

* **Importing Libraries**
    * Libraries for GUI have been imported- tkinter, ttk, messagebox.
    * Libraries for Database driver have been imported- sqlite.
    * Libraries for SMTP protocol have been imported- smtplib, MIMEMultipart, MIMEText.

* **Creating GUI Window**
    * Structure for the input of Visitor and Host Information.
    * It will contain Labels and its Entries, Buttons.

* **Connecting Database (SQLite)**
    * Driver helps in connecting Python with SQLite
    
* **Creating Tables Schemas**
    * Visitors and Hosts Tables schemas are created inside sqlite
    
* **Creating UI**
    * Labels and its Entries are created at the fornt-end of the application
    * These details are of both Visitors and Hosts.
  
* **Data Input**
    * Data is fed into the database for future use of sending mails.
    * Further, analysis can be done on this data.
   
* **Sending E-Mails**
    * Emails will be triggered to the Host regarding details of Visitor.
    * At checkout time, emails will be triggered to the Visitors.
    
* **Displaying Records(Data)**
    * Visitors and Hosts records are displayed seperately.
    * Buttons are provided at Front-End.
    
* **Creating Buttons**
    * Created a button for Input Data command.
    * Created a button for Displaying Visitors records.
    * Created a button for Displaying Hosts records.
