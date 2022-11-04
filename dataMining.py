# Data Mining

# Open the File to Read
myFile = open('USvideos.csv', encoding="utf-8")

# Read the data from file into a list
listOfLines = myFile.read().splitlines()
#print(listOfLines[0])
#print(listOfLines[1])
#print(listOfLines[len(listOfLines)-1])

#### SINGLE LINE ####
aLine = listOfLines[1]
lineItems = aLine.split(',')
print(lineItems)
date = lineItems[1]
data = lineItems[5]
#print('date=', date)
#print('data=', data)
dateSplit = date.split('.')
year = dateSplit[0]
month = dateSplit[2]
#print('year=', year)
#print('month=', month)
#### SINGLE LINE ####

oldMonth = month
sum = 0
count = 0
listOfAverages = []
output = int(float(data))
for i in range (1, len(listOfLines), 1):
    aLine = listOfLines[i]
    #print(aLine)
    lineItems = aLine.split(',')
    #print(lineItems)
    date = lineItems[1]
    data = lineItems[5]
    #print('date=', date)
    #print('data=', data)
    dateSplit = date.split('.')
    year = dateSplit[0]
    month = dateSplit[2]
    if month == oldMonth:
        count = count + 1   # count += 1
        sum = sum + output
        avg = sum / count
    #print('sum=', sum, 'count=', count, 'avg=', avg)
    if month != oldMonth or i == 40250:
        #print('year=', year, 'month=', oldMonth, 'avg=%.2f', avg)
        subList = [year, oldMonth, avg]
        listOfAverages.append(subList)
        sum = int(float(data))
        count = 1
        oldMonth = month
for i in range(0, len(listOfAverages), 1):
    print(listOfAverages[i])
