#Creating nested list
matrix =[[1,2,3],[4,5,6],[7,8,9]]
print(matrix)

#Accessing elements in a nested list
first_row_first_column = matrix[0][0] #Accesses 1
print("First row and first column value is:",first_row_first_column)

#USING THE PRINT FUNCTION WITH NESTED LISTS
#Pretty printing a Matrix
for row in matrix:
    print(row)

#Formatted output:
for row in matrix:
    print(''.join(map(str,row)))