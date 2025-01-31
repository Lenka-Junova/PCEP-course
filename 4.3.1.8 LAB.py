#4.3.8 LAB task - calculation of leap year and if inputed date is a leap year
def is_year_leap(year):
    if ((year%4 == 0) and (year%100 != 0)) or ((year%400 == 0) and (year%100 == 0)):
        return True
    else:
        return False
        
def days_in_month(year, month):
    current = month
    leap_year = is_year_leap(year)
    months = [31,28,31,30,31,30,31,31,30,31,30,31]
    if month <= 12 and month >= 1:
        if leap_year and month == 2:
            return 29
        else:
            return months[month-1]
    else:
        return None
        
def day_of_year(year, month, day):
    total_months = days_in_month(year, month)
    result = 0
    
    for days in range(1, month):
        total_months = days_in_month(year, days)
        result += total_months
        total_months = days_in_month(year, month)
            
    if (month < 1) or (month > 12):
        return None
    
    if (day > 0) and (day <= result):
        return result + day
    else:
	    return None
		
print(day_of_year(2000, 12, 31))
