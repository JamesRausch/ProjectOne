import csv
def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False
def is_leap(year):
    if is_even(year % 4) and is_even(year % 100)  and is_even(year % 400):
        return True
    else:
        return False
def days_in_year_prior(year,date,month):
    if(is_leap(year)):
        if(month == 'January') or (month == 1):
            return date
        elif(month == 'Feburary') or (month == 2):
            return date + 31
        elif(month == 'March') or (month == 3):
            return date + 29 + 31
        elif(month == 'April') or (month == 4):
            return date + 30 + 31 + 29
        elif(month == 'May') or (month == 5):
            return date + 30 + 30 + 31 + 29
        elif(month == 'June') or (month == 6):
            return date + 30 + 30 + 31 + 29 + 31
        elif(month == 'July') or (month == 7):
            return date + 30 + 30 + 31 + 29 + 31 + 30
        elif(month == 'August') or (month == 8):
            return date + 30 + 30 + 31 + 29 + 31 + 30 + 31
        elif(month == 'September') or (month == 9):
            return date + 30 + 30 + 31 + 29 + 31 + 30 + 31 + 30
        elif(month == 'October') or (month == 10):
            return date + 30 + 30 + 31 + 29 + 31 + 30 + 31 + 30 + 30
        elif(month == 'November') or (month == 11):
            return date + 30 + 30 + 31 + 29 + 31 + 30 + 31 + 30 + 30 + 31
        elif(month == 'December') or (month == 12):
            return date + 30 + 30 + 31 + 29 + 31 + 30 + 31 + 30 + 30 + 31 + 30
    else:
        if(month == 'January') or (month == 1):
            return date
        elif(month == 'Feburary') or (month == 2):
            return date + 31
        elif(month == 'March') or (month == 3):
            return date + 28 + 31
        elif(month == 'April') or (month == 4):
            return date + 30 + 31 + 28
        elif(month == 'May') or (month == 5):
            return date + 30 + 30 + 31 + 28
        elif(month == 'June') or (month == 6):
            return date + 30 + 30 + 31 + 28 + 31
        elif(month == 'July') or (month == 7):
            return date + 30 + 30 + 31 + 28 + 31 + 30
        elif(month == 'August') or (month == 8):
            return date + 30 + 30 + 31 + 28 + 31 + 30 + 31
        elif(month == 'September') or (month == 9):
            return date + 30 + 30 + 31 + 28 + 31 + 30 + 31 + 30
        elif(month == 'October') or (month == 10):
            return date + 30 + 30 + 31 + 28 + 31 + 30 + 31 + 30 + 30
        elif(month == 'November') or (month == 11):
            return date + 30 + 30 + 31 + 28 + 31 + 30 + 31 + 30 + 30 + 31
        elif(month == 'December') or (month == 12):
            return date + 30 + 30 + 31 + 28 + 31 + 30 + 31 + 30 + 30 + 31 + 30


def daysSince2014(day,month,year):
    if(year == 2014):
        return days_in_year_prior(year,day,month)
    elif((year == 2015)):
        return days_in_year_prior(year,day,month) + 356
    elif(year == 2016):
        return days_in_year_prior(year,day,month) + 356 + 356
    elif(year == 2017):
        return days_in_year_prior(year,day,month) + 366 + 356 + 356
    elif(year == 2018):
        return days_in_year_prior(year,day,month) + 366 + 365 + 356 + 356
    elif(year == 2019):
        return days_in_year_prior(year,day,month) + 366 + 365 + 365 + 356 + 356
    elif(year == 2020):
        return days_in_year_prior(year,day,month) + 366 + 365 + 365 + 365 + 356 + 356
    else:
        return print("outside of bound value")
def dayOfWeek(day,month,year):
    hold = 0
    if(year == 2014):
        hold = days_in_year_prior(year,day,month) + 3
    elif(year == 2015):
        hold = days_in_year_prior(year,day,month) + 4
    elif(year == 2016):
        hold = days_in_year_prior(year,day,month) + 5
    elif(year == 2017):
        hold = days_in_year_prior(year,day,month)
    elif(year == 2018):
        hold = days_in_year_prior(year,day,month) + 1
    elif(year == 2019):
        hold = days_in_year_prior(year,day,month) + 2

    if hold % 7 == 0 :
        return 0
    elif hold % 7 == 1:
        return 1
    elif hold % 7 == 2:
        return 2
    elif hold % 7 == 3:
        return 3
    elif hold % 7 == 4:
        return 4
    elif hold % 7 == 5 :
        return 5
    elif hold % 7 == 6 :
        return 6
    else:
        return "Invalid Input"
##Monday is 0, Sunday is 6
crime = open('crime.csv','r+')
newCrime = open('trafficCrime.csv','w',newline="")
catergories = [crime.readline().split(',')]
tempDataBase = []
for line in crime:
    linehold = line.rstrip().split(',')
    tempDataBase.append(linehold)
secondDatabase = []
for i in tempDataBase:
    if "\"traffic-accident\"" in i:
        secondDatabase.append(i)
writer = csv.writer(newCrime)
writer.writerows(secondDatabase)
newCrime.close()
sortCrime = open('trafficCrime.csv','r')
reader = csv.reader(sortCrime)
mydict = {rows[0]:rows[6] for rows in reader}
##Dict has rows with refrence id and date
newDict = {0:[],1:[],2:[],3:[],4:[],5:[],6:[]}
for i in mydict:
    stringHold = mydict[i]
    stringHoldTwo = stringHold.split(' ')
    stringHoldThree = stringHoldTwo[0]
    stringHoldThree = stringHoldThree[1:]
    stringHoldFour = stringHoldThree.split('/')
    day = int(stringHoldFour[1])
    month = int(stringHoldFour[0])
    year = int(stringHoldFour[2])
    newKey = dayOfWeek(day,month,year)
    ##Assign Hour to Day of Week
    hourHoldOne = stringHoldTwo[1]
    hourHoldTwo = hourHoldOne.split(':')
    hourHoldThree = hourHoldTwo[0]
    ##Check Am and PM
    amPMHold = stringHoldTwo[2]
    amPMHoldTwo = amPMHold[0:2]
    hourHoldThree = int(hourHoldThree)
    if amPMHoldTwo == "PM":
        hourHoldThree += 12
    newDict[newKey].append(hourHoldThree)
def accidentsInHour(weekday,hour):
    count = 0
    for i in newDict[weekday]:
        if i == hour:
            count += 1
    return count
weekday = input("Please enter the target weekday with Monday being 0 and Sunday being 6 as an integer between 0 and 6: ")
weekday = int(weekday)
hour = input("Please enter the target hour ranging from 0 to 23: ")
hour = int(hour)
print(accidentsInHour(weekday,hour))
        
