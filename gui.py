# Importing specific needed libraries
import datetime
from tkinter import *
from tkcalendar import *

# Prepare user's current date for program use
today = datetime.datetime.now()

# Create title and size
root = Tk()
root.title("CIS30A Business Program")
root.geometry("600x400")

# This is where the program sets the date for the calendar with the use of datetime
# Will be user's current date
cal = Calendar(root, selectmode="day", year=2021, month= int(today.strftime("%m")), day = int(today.strftime("%d")))
cal.pack(pady=20, fill="both", expand = True)

# Will grab selected date and will show the user
#   -> Will be used for object creations and others
def grabDate():
    selectedDate.config(text=cal.get_date())

# Label for grabDate button
my_button = Button(root, text = "Get Date", command = grabDate)
my_button.pack(pady=20)

# Label for showing date
selectedDate = Label(root, text = "")
selectedDate.pack(pady=20)

# Program loop
root.mainloop()