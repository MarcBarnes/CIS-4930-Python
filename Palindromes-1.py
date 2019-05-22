'''  mbb11d
	MARCUS BARNES PYTHON ASSIG1
	Palindromes.py

	this program takes in input 
		Specification on input:
			each line is considered a single item
			add string to dictionary
			key= counter, value = string value
			ignore spaces
			ignore cases
		Ideas:
			two or three sets of dicktionariesa, 
				one to place in all original input
				second to place all modified list with no spaces and all lowercase
				third to place all of the second in reverse order
			compare item to item list 2 and list 3
			if they are equal, then print the item in list 1

'''

##four empty dictionaries. d1-d3 are syncronous
d1 = {}		#holds OG dict
d2 = dict()	#holds lowercased and space free version of d1
d3 = {}		#holds reversed version of d2
d4 = {}		#holds only the items that are palindromes

print ("Enter the strings: ")
tempItem = ""
counter = 0
while tempItem != "Done":
	tempItem = input ()
	if tempItem != "Done":
		d1[counter] = tempItem #adding item to first dictionary
		counter += 1 

d2 = d1.copy()#copying d1 to d2

#loop to change each value to lowercase and remove spaces in d2
#then flipping d2 and placing into d3
paliCounter= 1
for x in d2:
	d2[x] = d2.get(x).lower()
	d2[x] = d2.get(x).replace(" ", "")
	d3[x] = ''.join(reversed(d2.get(x)))
	if d2.get(x) == d3.get(x):
		d4[paliCounter] = d1.get(x)
		paliCounter += 1

print("The palindromes are:\n", d4)