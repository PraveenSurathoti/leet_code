def rotate(matrix):
	n = len(matrix)
	for row in range(n):
		for col in range(row,n):
			matrix[col][row],matrix[row][col]=matrix[row][col],matrix[col][row]
    for row in matrix:
        reverse(row)
    return matrix
    
	
	
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate(matrix))
