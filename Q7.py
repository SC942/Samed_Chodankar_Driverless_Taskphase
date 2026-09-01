from pointProximity import pointProximity

points=[]

n = int(input("Enter the number of points you have: "))

print("Enter the 2D coordinates of points(separated by spaces)- ")

for i in range(1 ,n+1):
    coords = input(f"Enter point{i}: ").strip().split()
    x = float(coords[0])
    y = float(coords[1])
    points.append((x,y))

refCoords = input("Enter reference point coordinates(separated by spaces): ").strip().split()
refPoint = (float(refCoords[0]), float(refCoords[1]))

findDistance = pointProximity()

sortedPoints = findDistance.sortCoords(points, refPoint)

print("Sorted points by proximity: ", sortedPoints)