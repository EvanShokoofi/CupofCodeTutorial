#Day11


#takes 2 digits (m and n, row and col respectively) as inputs and generates a 2d array.
#The element value in the i-th row and j-th column of the array should be i*j

row_num = int(input('How many rows: '))
col_num = int(input('How many columns: '))
list = [[0 for col in range(col_num)] for row in range(row_num)]

for row in range(row_num):
	for col in range(col_num):
		list[row][col] = row*col
print(list, '\n')


#write a Python program that accepts a sequence of lower case lines (blank line to terminate) as input
# and prints the lines as output (all characters in upper case)

lines = []
while True:
	l = input()
	if l:
		lines.append(l.lower())
	else:
		break;
for l in lines:
	print(l)


#write a program which accepts a sequence of comma separated 4 digit binary numbers as its input
# and print the numbers that are divisible by 5 in a cs sequence.

def divividable_binary():
	s = input('Enter the binaries: ')
	l = s.split(',')
	for i in l:
		if int(str(i),2) % 5 == 0:
			print('Output: ',i)
divividable_binary()

