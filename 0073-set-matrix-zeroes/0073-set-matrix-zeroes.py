class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])

        first_row = False
        first_col = False

        for i in range(m):
            if matrix[i][0] == 0:
                first_col = True
        
        for j in range(n):
            if matrix[0][j] == 0:
                first_row = True

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
            
        for i in range(1, m):
            for j in range(1, n):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
                
        if first_row:
            for i in range(n):
                matrix[0][i] = 0

        if first_col:
            for j in range(m):
                matrix[j][0] = 0
        
        return matrix

        