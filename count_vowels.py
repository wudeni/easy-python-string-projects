#Count Vowels
#Enter a string/ or txt file and the program counts the number of vowels in the text.
#And also it reports a sum of each vowel found.

import string
fname = input('Enter the file name: ')
print('\n')

# Opening a file
try:
	fhand = open(fname)
except:
	print('File cannot opened:' , fname)
	exit()

# Reading a file, counting words using dictionary
vow = ['a', 'e', 'i', 'o', 'u'] # Assigning a list of vowels
counting_vows ={}.fromkeys(vow,0) #Assigning a dictionary
count = 0 # total number of vowels

for line in fhand:
	line = line.rstrip()
	line = line.translate(line.maketrans('', '', string.punctuation)) #remove punctuations
	line = line.lower() #transfer upper to lower case
	words = line.split()
	for word in words:
		for letter in word:
			if letter in vow:
				count += 1
				counting_vows[letter] +=1
				
lst_vows = list(counting_vows.keys())
lst_vows.sort()

for key in lst_vows:
	print(key, counting_vows[key])

print('Total vowels ', count)	