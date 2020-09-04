import os #for various file manipulation methods
import shutil #will be used to move files

#Tutorial is run based on the presence of newUser.txt in the program directory.
def newUser():
	os.system('TUTORIAL.py')
	os.remove('newUser.txt')
	quit()

if os.path.isfile('newUser.txt'):
	newUser()

#Main functionality begins here. User's input from tutorial is read.
tag_text = open('sortTags.txt', 'r')
tag_list = tag_text.read().splitlines()
to_text = open('sortDirs.txt', 'r')
to_list = to_text.read().splitlines()
from_text = open('sourceDirs.txt', 'r')
from_list = from_text.read().splitlines()

#All files found in source directories are appended to from_dirscan.
from_dirscan = []
for directory in from_list:
	for item_entry in os.scandir(directory %('')):
		from_dirscan.append(item_entry)

#This is the faster version of the program. It runs without giving and asking for user confirmation.
#On when noCheck.txt is in the program directory. Without noCheck.txt, full version runs.
def noCheck():
	i = 0
	for tag in tag_list:
		for item in from_dirscan:
			if item.name.startswith(tag_list[i]):
				shutil.move(item, to_list[i] %(item.name))
		i += 1
if os.path.isfile('noCheck.txt'):
	noCheck()
	quit()

#This is the full version of the program, which gives and requests user confirmation.
i = 0 #An increment of 'i' moves the program along the list of tags. 
move_list=[] #This list is presented to the user in the confirmation dialogues further down.
for tag in tag_list: 
	for item in from_dirscan:
		if item.name.startswith(tag_list[i]): 
			move_list.append(item)
	i += 1	#This indentation level means that 'i' is incremented once all items have been scanned for a certain tag.
			#After 'i' is incremented, the tag scan is repeated with the next position on the tag list.

def dsmove(): #Core of the program.
	i = 0
	for tag in tag_list: #Same process as earlier but ends with items being moved and confirmation
			for item in from_dirscan:
				if item.name.startswith(tag_list[i]):
					shutil.move(item, to_list[i] %(item.name))
					print(item.name, "has been moved to", to_list[i])
			i += 1

print(len(move_list), "tagged items have been found.") #User gets a chance to review results before moving files.
if input("Would you like to review a list of these? y/n:   ") == 'y':
	for item in move_list:
		print(item.name)
	if input("Would you like to move these items? y/n:   ") == 'y':
		dsmove()
else:
	if input("Would you like to move these items? y/n:   ") == 'y':
		dsmove()
	




#hello plis this is tecnikil snitzil and i will do many tecnikil thingses yes yes like delete the internets and also many other thingses like install the program of making beautifuls with computers

#The program checks all entries from the source directories for the user-defined tags.
	#This check is repeated as many times as there are tags.
	#An increment of 'i' makes the program check for the tag which is on the next line in sortTags.txt.
	#For this to work properly, the list of tags and the list of sort directories must be in the same order.
	#i.e.  Once found, tagged files are sent off to their respective directories, 