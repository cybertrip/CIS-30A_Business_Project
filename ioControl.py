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
	file = open("schedule.text", "a")
	
	#subject, destination, expected, conpany
	file.write(schedule.subject + " ")
	file.write(schedule.destination + " ")
	file.write(schedule.expected + " ")
	file.write(schedule.company + " ")

	if(type == "appointment"):
		print("This is appointment")
		# contact, hours=None, room=None, agent=None
		file.write(schedule.contact + " ")
		file.write(schedule.hours + " ")
		file.write(schedule.room + " ")
		file.write(schedule.agent + "\n")

	elif(type == "delivery"):
		print("This is delivery")
		# tracking, origin, departed, items
		file.write(schedule.tracking + " ")
		file.write(schedule.origin + " ")
		file.write(schedule.departed + " ")
		file.write(schedule.items + "\n")