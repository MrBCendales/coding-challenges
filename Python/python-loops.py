#Task
#The provided code stub reads an integer, , from STDIN. For all non-negative integers , print .

#Example n=3

#The list of non-negative integers that are less than  is . Print the square of each number on a separate line.
#

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i**2)

# An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.

# In the Gregorian calendar, three conditions are used to identify leap years:

# The year can be evenly divided by 4, is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap year.
# This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years. Source

# Task

# Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.

# Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.

def is_leap(year):
    leap = False
    
    # Write your logic here
    if not year % 4:
        if not year % 100:
            if not year % 400:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
            leap = False      
    return leap

year = int(input())


n = int(input()) 
string = "" 
for i in range(n):
    string += str(i+1) 
print(string)