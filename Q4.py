from inputMatrix import inputMatrix
from multiplyMatrices import multiplyMatrices

getInput = inputMatrix()
matrixA = getInput.takeInput("A")
matrixB = getInput.takeInput("B")

multiply = multiplyMatrices()
result = multiply.matMult(matrixA, matrixB)

print("The resulting matrix = ")
for row in result:
    print(row)