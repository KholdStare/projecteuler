#!/usr/bin/python

daysInMonth = [ 31,
                28,
                31,
                30,
                31,
                30,
                31,
                31,
                30,
                31,
                30,
                31 ] 

def is_leap_lear(year):
    if year%4 == 0:
        if year%100 == 0: #century
            if year%400 == 0:
                return True

        else:
            return True

    return False

def days_in_month(month, isLeap):
    index = month-1
    if isLeap and index == 1:
        return daysInMonth[index] + 1

    return daysInMonth[index]

def main (startYear, endYear):
    day = 1 # January 1st 1900 is a Monday
    month = 1
    sundayCount = 0
    for year in xrange(1900, endYear+1):
        isLeap = is_leap_lear(year)

        for month in xrange(1, 13):
            if year >= startYear and day%7 == 0:
                sundayCount += 1

            day += days_in_month(month, isLeap)

    return sundayCount



if __name__ == "__main__":
    print main(1901, 2000)
