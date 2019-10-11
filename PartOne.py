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
                
                
def daysSince2016(day,month,year):
     if(year == 2016):
        return days_in_year_prior(year,day,month)
     elif(year == 2017):
         return days_in_year_prior(year,day,month) + 366
     elif(year == 2018):
         return days_in_year_prior(year,day,month) + 366 + 365
     elif(year == 2019):
        return days_in_year_prior(year,day,month) + 366 + 365 + 365
     elif(year == 2020):
         return days_in_year_prior(year,day,month) + 366 + 365 + 365 + 365
     else:
            return print("outside of bound value")
print(weekValue(21,3,2017))
def dayOfWeek(day,month,year):
       hold = daysSince2016(day,month,year)
       if hold % 7 == 0 :
         return "Sunday"
       elif hold % 6 ==0:
            return "Monday"
       elif hold % 5 == 0:
            return "Tuesday"
       elif hold % 4 == 0:
          return "Wensday"
       elif hold % 3 == 0:
         return "Thursday"
       elif hold % 2 == 0 :
                return "Friday"
       elif hold % 1 == 0 :
            return "Saturday"
       else:
            return "Invalid Input"
    
print(is_leap(2016))
print(days_in_year_prior(2017,21,3))
print(daysSince2016(21,3,2017))
print(dayOfWeek(11,10,2019))
## 
