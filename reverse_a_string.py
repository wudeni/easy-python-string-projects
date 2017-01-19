import string
name = input('Enter your Name:- ')
lst = list()
name = name.lower()
for char in name:
	lst.append(char)
delimiter = ''
lst = delimiter.join(lst[::-1]).title()
print('Your alien name is :', lst)
