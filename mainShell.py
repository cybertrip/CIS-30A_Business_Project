from prompts import *

# Run the welcome user prompt for startup of program
welcomeUser()
# Used to space out text from eachother for better readability
print()

# Ask user if they want a new appointment created
askCreateSchedule("appointment")
print()

# Ask user if they want a new delivery created
askCreateSchedule("delivery")
print()

# Ask user if they want to delete a schedule from the file
askDeleteSchedule()
print()

# Ask user if they want to read all schedules from the file
askReadSchedule()
print()

# End the program and let the user know
farewellUser()