inFile = open("billboard.in", "r")
ints = []
#Reading file values
for val in inFile.read().split():
    ints.append(int(val))
inFile.close()
#Bilboard1 coordinates
bbXmin = ints[0]
bbYmin = ints[1]
bbXmax = ints[2]
bbYmax = ints[3]
#Truck coordinates
truckXmin = ints[8]
truckYmin = ints[9]
truckXmax = ints[10]
truckYmax = ints[11]
#Calculating bilboard area
def area(xmax, xmin, ymax, ymin):
    area = (xmax - xmin) * (ymax - ymin)
    return area

#Finding x and y overlap length
def checkoverlap(line1Min, line1Max, line2Min, line2Max):
    if(line2Max < line1Min or line2Min > line1Max):
        return int(0)
    point1 = max(line1Min, line2Min)
    point2 = min(line1Max, line2Max)
    return point2 - point1
#Visibily for first bilboard
bbxLen = checkoverlap(bbXmin, bbXmax, truckXmin, truckXmax)
bbyLen = checkoverlap(bbYmin, bbYmax, truckYmin, truckYmax)
overlap = bbxLen * bbyLen
bbarea = area(bbXmax, bbXmin, bbYmax, bbYmin)
bb1Vis = bbarea - overlap
#Bilboard2 coordinates
bbXmin = ints[4]
bbYmin = ints[5]
bbXmax = ints[6]
bbYmax = ints[7]
#Visibily for second bilboard
bbxLen = checkoverlap(bbXmin, bbXmax, truckXmin, truckXmax)
bbyLen = checkoverlap(bbYmin, bbYmax, truckYmin, truckYmax)
overlap = bbxLen * bbyLen
bbarea = area(bbXmax, bbXmin, bbYmax, bbYmin)
bb2Vis = bbarea - overlap
#Total visibilty
totalArea = bb1Vis + bb2Vis
#Writing value in file

file = open("billboard.out", "w+")
file.write(str(totalArea))
file.close()
