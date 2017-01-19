#Enter a string & this python program will reverse it and print it
name = input('Enter your Name:- ')
lst = list()
for char in name:
	lst.append(char)
delimiter = ''
lst = delimiter.join(lst[::-1]).title()
print('Your alien name is :', lst)
