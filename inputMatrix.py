class inputMatrix:
    def takeInput(self, name):
        r = int(input("Enter the number of rows in the matrix: "))
        c = int(input("Enter the number of columns in the matrix: "))

        matrix = []

        print(f"Enter elements of {name} row-by-row(separated by spaces): ")

        for i in range(r):
            while True:
                rowStr = input(f"Row {i+1} = ").strip().split()
                if len(rowStr) != c:
                    print(f"ERROR: You must enter exactly {c} values.")
                    continue
                try:
                    row = [float(val) for val in rowStr]
                    matrix.append(row)
                    break
                except ValueError:
                    print("ERROR: Invalid Entry. Only enter numbers.")

        return matrix
        