# This will be where the introduction to the program will be located
#   -> How the program works
#   -> What the program is
#   -> User interface controls
# ioControl is the module for displaying to shell/terminal
# schedule is the module responsible for class parent and child inheritence/arguments
import datetime
from ioControl import *
from schedule import *



# Bring in global variables from schedule.py to access across all functions
# These will be the dPrint standard delay values
global stdDelay
global stdSpace



# Welcome the user to the program
#   No instructions, just a simple greeting
#   Prints the current date and time to the user
def welcomeUser():
    dPrint("Hello user", stdSpace, 0)  # override time delay/space
    dPrint("...\n", 0.555, 0)  # override time delay/space
    dPrint("Welcome to the CIS30A Python Business Program!\n", stdSpace, stdDelay)
    dPrint("\t-> Otherwise known as an appointment/delivery scheduler.\n\n", stdSpace, stdDelay)
    today = datetime.datetime.now()
    dPrint("Today is " + today.strftime("%B %d, %Y") + ".\n", stdSpace, stdDelay)
    dPrint("The time is " + today.strftime("%H:%I:%S %p") + ".\n", stdSpace, stdDelay)



# Farewell the user
#   Program has ended, so let the user know
def farewellUser():
    dPrint("Thank you for using the program.\n", stdSpace, stdDelay)
    dPrint("Run it again if you would like schedule some more.", stdSpace, stdDelay)



# Ask the user if they want to schedule an appointment or delivery (decided by string type)
# Send the user to create the decided object due to their response
def askCreateSchedule(type):
    # Bring in global variables from schedule.py to function
    # This makes it locally accessible
    global scheduleCounter
    global objectList

    # Declare response string that is empty
    response = ""

    # Ask the user if they want to create the schedule of the parameter type
    #   -> Will repeat question until their response is correct
    dPrint("Would you like to schedule a(n) " + type + "?\n", stdSpace, stdDelay)
    # Start loop to run indefnitely
    #   Will break if receiving "yes" or "no"
    while True:
        # Ask user for their response input (as string)
        response = input("Enter 'yes' or 'no':\t")
        # try-exception check
        #   If we get "yes" or "no" then break
        #   Else return the exception error
        try:
            # If "yes" or "no" then break
            if(response.lower() == "yes" or response.lower() == "no"):
                break
            # Else raise an input exception
            else:
                raise Exception
        # Input exception
        except Exception:
            # Tell user the input was invalid/not desired
            print("That input is invalid, try again.")

    # If user wants to create a schedule (response is 'yes')
    #   -> Then continue with the program prompted schedulr either appointment or delivery
    # Appointment or delivery is defined by the parameter type
    if (response.lower() == "yes" and type == "appointment"):
        # type is defined as schedule type, in this case being 'appointment'
        createSchedule(type)

    elif (response.lower() == "yes" and type == "delivery"):
        # type is defined as schedule type, in this case being 'delivery'
        createSchedule(type)



# Area to create objects from the classes
def createSchedule(type):
    # Bring in global variables from schedule.py to function
    # This makes it locally accessibles
    global scheduleCounter
    global objectList

    # Ask user to create variable that is a name of the object
    dPrint("Please enter a reference name: ", stdSpace, stdDelay)
    input_name = input()

    # Add new variable to objectList
    objectList.append(input_name)

    # Check if creating appointment or delivery object
    #   True is appointment
    #   False is delivery
    if (type == "appointment"):
        # Convert variable name to object
        objectList[scheduleCounter] = appointment()

        # Assign arguments to class object
        # Ask user what they want
        dPrint("What is the appointment name?\t", stdSpace, stdDelay)
        objectList[scheduleCounter].subject = input()

        dPrint("Where is the appointment?\t", stdSpace, stdDelay)
        objectList[scheduleCounter].destination = input()

        dPrint("What time is the appointment?\t", stdSpace, stdDelay)
        objectList[scheduleCounter].expected = input()

        dPrint("What is the name of the company?\t", stdSpace, stdDelay)
        objectList[scheduleCounter].company = input()

        dPrint("What is the contact of the company?\t", stdSpace, stdDelay)
        objectList[scheduleCounter].contact = input()

        dPrint("What is the operating hours of the company?\t", stdSpace, stdDelay)
        objectList[scheduleCounter].hours = input()

        dPrint("What is the room number?\t", stdSpace, stdDelay)
        objectList[scheduleCounter].room = input()

        dPrint("Who are you meeting?\t", stdSpace, stdDelay)
        objectList[scheduleCounter].agent = input()

    elif (type == "delivery"):
        # Convert variable name to object
        objectList[scheduleCounter] = delivery()

        # Assign arguments to class object
        # Ask user what they want
        dPrint("What is the name of the delivery?\t", stdSpace, stdDelay)
        objectList[scheduleCounter].subject = input()

        dPrint("Where is the delivery going?\t", stdSpace, stdDelay)
        objectList[scheduleCounter].destination = input()

        dPrint("When is the expected date of the delivery?\t", stdSpace, stdDelay)
        objectList[scheduleCounter].expected = input()

        dPrint("What is the name of the company?\t", stdSpace, stdDelay)
        objectList[scheduleCounter].company = input()

        dPrint("What is the tracking number of the delivery?\t", stdSpace, stdDelay)
        objectList[scheduleCounter].tracking = input()

        dPrint("Where is the shipping origin of the delivery?\t", stdSpace, stdDelay)
        objectList[scheduleCounter].origin = input()

        dPrint("When did the delivery depart?\t", stdSpace, stdDelay)
        objectList[scheduleCounter].departed = input()

        dPrint("What items are being delivered?\t", stdSpace, stdDelay)
        objectList[scheduleCounter].items = input()

    # Increment scheduleCounter by 1 for new object if so repeated and created
    scheduleCounter += 1

    # Ask user if they want to write their schedule to the file
    askWriteSchedule(type)



# Ask user if they want to write a schedule to the text file
def askWriteSchedule(type):
    # Bring in global variables from schedule.py to function
    # This makes it locally accessible
    global scheduleCounter
    global objectList

    # Declare response string that is empty
    response = ""

    # Ask the user if they want to store their schedule into a file
    #   -> Will repeat question until their response is correct
    dPrint("Would you like to put your " + type + " into a file?\n", stdSpace, stdDelay)
    # Start loop to run indefnitely
    #   Will break if receiving "yes" or "no"
    while True:
        # Ask user for their response input (as string)
        response = input("Enter 'yes' or 'no':\t")
        # try-exception check
        #   If we get "yes" or "no" then break
        #   Else return the exception error
        try:
            # If "yes" or "no" then break
            if(response.lower() == "yes" or response.lower() == "no"):
                break
            # Else raise an input exception
            else:
                raise Exception
        # Input exception
        except Exception:
            # Tell user the input was invalid/not desired
            print("That input is invalid, try again.")

    # Send user to write their schedule to a file based on the type and response
    if (response.lower() == "yes" and type == "appointment"):
        # type is defined as schedule, in this case being 'appointment'
        writeSchedule(type, objectList[scheduleCounter - 1])

    elif (response.lower() == "yes" and type == "delivery"):
        # type is defined as schedule, in this case being 'delivery'
        writeSchedule(type, objectList[scheduleCounter - 1])



# Ask user if they want to read their file full of schedules
def askReadSchedule():
    # Declare response string that is empty
    response = ""

    # Ask the user if they want to read their file
    #   -> Will repeat question until their response is correct
    dPrint("Would you like to read all your schedules in your file?\n", stdSpace, stdDelay)
    # Start loop to run indefnitely
    #   Will break if receiving "yes" or "no"
    while True:
        # Ask user for their response input (as string)
        response = input("Enter 'yes' or 'no':\t")
        # try-exception check
        #   If we get "yes" or "no" then break
        #   Else return the exception error
        try:
            # If "yes" or "no" then break
            if(response.lower() == "yes" or response.lower() == "no"):
                break
            # Else raise an input exception
            else:
                raise Exception
        # Input exception
        except Exception:
            # Tell user the input was invalid/not desired
            print("That input is invalid, try again.")

    # Send user to write their schedule to a file based on the type and response
    if (response.lower() == "yes"):
        # Go to read file in ioControl
        listSchedule()



# Ask user if they want to delete a schedule from the file
def askDeleteSchedule():
    # Declare response string that is empty
    response = ""

    # Ask the user if they want to delete a schedule from the file
    #   -> Will repeat question until their response is correct
    dPrint("Would you like to delete a schedule from the file?\n", stdSpace, stdDelay)
    # Start loop to run indefnitely
    #   Will break if receiving "yes" or "no"
    while True:
        # Ask user for their response input (as string)
        response = input("Enter 'yes' or 'no':\t")
        # try-exception check
        #   If we get "yes" or "no" then break
        #   Else return the exception error
        try:
            # If "yes" or "no" then break
            if(response.lower() == "yes" or response.lower() == "no"):
                break
            # Else raise an input exception
            else:
                raise Exception
        # Input exception
        except Exception:
            # Tell user the input was invalid/not desired
            print("That input is invalid, try again.")

    if(response.lower() == "yes"):
        # Go to read file in ioControl
        lMin, lMax = listSchedule()

        # Declare response that is empty (This time int)
        response = 0

        # Ask the user which schedule they want to delete from the file
        #   -> Will repeat question until their response is correct
        dPrint("Which schedule would you like to delete from the file?\n", stdSpace, stdDelay)
        # Start loop to run indefnitely
        #   Will break if receiving "yes" or "no"
        while True:
            # Ask user for their response input (as string)
            response = int(input("Enter a visible number.\t"))
            # try-exception check
            #   If we get a number within range then break
            #   Else return the exception error
            try:
                # If number within range then break
                if(response >= lMin and response < lMax):
                    break
                # Else throw exception
                else:
                    raise Exception
            # Input exception
            except Exception:
                # Tell user the input was invalid/not desired
                print("That input is invalid, try again.")

        # Delete specfic line that user inputted
        deleteSchedule(response)