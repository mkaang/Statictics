def is_symmetric(matrix):
    sym = True
	if matrix.shape[0] != matrix.shape[1]: 
		sym = False
    else:
        for i in range(matrix.shape[0]):
    		for j in range(matrix.shape[1]):
    			if matrix[i,j] != matrix[j,i]:
                    sym = False
                else:
                    return True

