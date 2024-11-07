# Name: Kaden Billin
# Lab Section: 12
# Submission Date: 11/6/24
# Sources, help given to/received from:

month_lengths = {
    "01": 31,
    "02": 28,
    "03": 31,
    "04": 30,
    "05": 31,
    "06": 30,
    "07": 31,
    "08": 31,
    "09": 30,
    "10": 31,
    "11": 30,
    "12": 31,
    }

week_days = {
     "Sunday": 0,
     "Monday": 1,
     "Tuesday": 2,
     "Wednesday": 3,
     "Thursday": 4,
     "Friday": 5,
     "Saturday": 6
    }

year = input("Please input a date in the format MM/DD/YYYY: ")
yeardict = (year.split("/"))


y = int(yeardict[2])
if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0): 
    print(f"{y} is a leap year.")
else:
     print(f"{y} is not a leap year.")


print(month_lengths["01"])