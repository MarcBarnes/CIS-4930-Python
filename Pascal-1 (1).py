''' mbb1d
	Pascal.py
	Marcus Barnes
	HW 1 pt.2
	9/15/18

'''
lineInput = input("Enter the number of rows: ")
print("You entered:", lineInput)
numOfLines = int(lineInput)						#casting input to an int


#base case
print("1\n1 1\n1 2 1")
prevlist = [1, 2, 1] 

#printing w/o the \n character
#I should normally import deque and front pop
#but we shouldnt import LIBRARIES for THIS HW
##main loop
ln = 4
while ln <= numOfLines:
	newlist = [1] #declares first newlist and reformats newlist
	item = 1		#and first item in newlist is always 1
	print (newlist[0], end = " ")
	while item <= (ln - 2): #loops through all the items on the prevline and creates items newline
		newlist.append(prevlist[item -1] + prevlist[item])
		print(newlist[item], end = ' ')
		item += 1
	newlist.append(1)	#appends the last item is always 1
	print(1)
	prevlist= newlist.copy() #copys from newlist to mylist
	newlist = [1]			#reformats newlist to [1]
	ln += 1

	
	

	
