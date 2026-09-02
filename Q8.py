import csv
import math

def processCones(inputCsv, blueCsv, yellowCsv, centrelineCsv):
    def distFromOrigin(row):
        return math.hypot(float(row['x']), float(row['y']))

    with open(inputCsv, mode = 'r', encoding = 'utf-8') as infile:
        reader = csv.DictReader(infile)
        sortedRows = sorted(reader, key = distFromOrigin)

    blueCones = []
    yellowCones = []

    with open(blueCsv, mode = 'w', newline = '', encoding = 'utf-8') as bFile, \
        open(yellowCsv, mode = 'w', newline = '', encoding = 'utf-8') as yFile:

        filednames = ['coneId', 'x', 'y', 'colour']
        bWriter = csv.DictWriter(bFile, fieldnames = filednames)
        yWriter = csv.DictWriter(yFile, fieldnames = filednames)

        bWriter.writeheader()
        yWriter.writeheader()

        for row in sortedRows:
            if row['colour'].lower() == 'blue':
                bWriter.writerow(row)
                blueCones.append(row)
                
            elif row['colour'].lower() == 'yellow':
                yWriter.writerow(row)
                yellowCones.append(row)

    midpoints = []
    for blue in blueCones:
        bx, by = float(blue['x']), float(blue['y'])
        minDist = float('inf')
        nearestYellow = None

        for yellow in yellowCones:
            yx, yy = float(yellow['x']), float(yellow['y'])
            dist = math.hypot(bx - yx, by - yy)
            if dist < minDist:
                minDist = dist
                nearestYellow = (yx, yy)

        if nearestYellow is not None:
            midx = (bx + nearestYellow[0])/2
            midy = (by + nearestYellow[1])/2
            midpoints.append({'midx': midx, 'midy': midy})

    with open(centrelineCsv, mode = 'w', newline = '', encoding = 'utf-8') as cFile:
        cWriter = csv.DictWriter(cFile, fieldnames = ['midx', 'midy'])
        cWriter.writeheader()
        cWriter.writerows(midpoints)


if __name__ == "__main__":
    processCones("cones.csv", "blueCones.csv", "yellowCones.csv", "centreline.csv")
