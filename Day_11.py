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


