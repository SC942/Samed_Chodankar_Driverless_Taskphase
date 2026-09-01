class multiplyMatrices:
    def matMult(self, A, B):
        rowsA = len(A)
        colsA = len(A[0])
        rowsB = len(B)
        colsB = len(B[0])
        
        if colsA != rowsB:
            print("Multiplication is not possible between these 2 matrices")
            return None

        result = [[0 for i in range(colsA)] for i in range(rowsA)]

        for i in range(rowsA):
            for j in range(colsB):
                for k in range(colsA):
                    result[i][j] += A[i][k] * B[k][j]

        return result
