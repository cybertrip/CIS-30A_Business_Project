# Imported libraries
import sys
import time



#stdDelay = 1.25
stdDelay = 0 #debug-override
#stdSpace = 0.0625
stdSpace = 0 #debug-override



# Print to shell/terminal
def dPrint(string, seconds, wait):
    for character in string:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(seconds)
    time.sleep(wait)



# Write to text file
def writeSchedule(type, schedule):
    file = open("schedule.txt", "a")
    
    #subject, destination, expected, conpany
    file.write("Subject: " + schedule.subject + ", ")
    file.write("Destination: " + schedule.destination + ", ")
    file.write("Expected: " + schedule.expected + ", ")
    file.write("Company: " + schedule.company + ", ")

    if(type == "appointment"):
        # contact, hours, room, agent
        file.write("Contact: " + schedule.contact + ", ")
        file.write("Hours: " + schedule.hours + ", ")
        file.write("Room: " + schedule.room + ", ")
        file.write("Agent: " + schedule.agent + ".\n")

    elif(type == "delivery"):
        # tracking, origin, departed, items
        file.write("Tracking: " + schedule.tracking + ", ")
        file.write("Origin: " + schedule.origin + ", ")
        file.write("Departed: " + schedule.departed + ", ")
        file.write("Items: " + schedule.items + ".\n")

    # Close file
    file.close()



# List schedules from text file by number
def listSchedule():
    # Open the scheduule file to read
    file = open("schedule.txt", "r")
    
    # Store all read lines into variable lines
    lines = file.readlines()
    
    # lMin (line minimum) is the starting line number which is always 1
    lMin = 1
    
    # lMax (line maximum) is the ending line number which is changing to the amount of lines there are in the file
    lMax = 1
    
    # For loop to traverse the file and print every line at a time
    for level in lines:
        print(lMax,")\t", end="")
        print(level)
        lMax += 1
    
    # Close the file
    file.close()
    
    # Return the starting line and ending line numbers respectively
    return lMin, lMax



# Delete a schedule from the text file with line 'seeked'
#   -> seeked is the line number the user chooses to delete from the tet file
def deleteSchedule(seeked):
    # Open the schedule file to read
    file = open("schedule.txt", "r")
    
    # Read the lines of the file into a variable
    lines = file.readlines()
    
    # count will be the iteration level of the lines (starting at 1) in the file
    count = 1
    
    # saved will store all non-deleted lines
    saved = []
    
    # This for loop will run through every line of the file
    #   -> If the line is equal to the user defined deleted line, then do not save it
    #   -> Otherwise it will save it
    #   -> Then increments count by 1 till file is read line by line
    for level in lines:
        if(count != seeked):
            saved.append(level)
        count += 1
        
    # Close the file
    file.close()
    
    # Open the file this time overwriting it
    file = open("schedule.txt", "w")
    
    # Transfer contents of saved to the file
    file.writelines(saved)
    
    # Close the file
    file.close()