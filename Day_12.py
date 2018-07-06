#Day12


#accept a string and calculate number of letters and digits

s = input('give me a string:')
l, d = 0,0
for c in s:
	if c.isalpha():
		l=l+1
	elif c.isdigit():
		d=d+1
	else:
		pass
print('Letters', l)
print('Digits', d)


#check the validity of a password
#at least 1 [a-z] and 1 [A-Z]
#at least 1 number [0-9]
#at least 1 special character [$#@]
#min 6 characters, max 16

import re #Regular expressions for matching
p = input('enter password: ')
x = True

while x:
	if (len(p)<6 or len(p)>16):
		break
	elif not re.search('[a-z]', p):
		break
	elif not re.search('[0-9]', p):
		break
	elif not re.search('[A-Z]', p):
		break
	elif not re.search('[$#@]', p):
		break
	elif re.search('\s', p):
		break
	else:
		print('password check is a green light')
		x = False
		break
if x:
	print("that is a BS password - you are banned for life")


#find numbers between 100 and 400(both included, where each digit is even)
#print in csv sequence

even_digits = []
for i in range(100,401):
	s = str(i)
	if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0):
		even_digits.append(s)
print(' $$$ '.join(even_digits))


#create a program that will print out a pattern of an 'A'

Letter_A = ''
for row in range(0,7):
	for column in range(0,7):
		if (((column == 1 or column == 5) and row !=0) or ((row==0 or row==3) and (column > 1 and column < 5))):
			Letter_A = Letter_A + '*'
		else:
			Letter_A = Letter_A + ' '
	Letter_A = Letter_A + '\n'
print(Letter_A)

