# Name: Kaden Billin
# Lab Section: 12
# Submission Date: 11/7/24
# Sources, help given to/received from:

month_lengths = {
    "01": ["January", 1, 31],
    "02": ["February", 2, 28],
    "03": ["March", 3, 31],
    "04": ["April", 4, 30],
    "05": ["May", 5, 31],
    "06": ["June", 6, 30],
    "07": ["July", 7, 31],
    "08": ["August", 8, 31],
    "09": ["September", 9, 30],
    "10": ["October", 10, 31],
    "11": ["November", 11, 30],
    "12": ["December", 12, 31]
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

valid = True
y = int(yeardict[2])

if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
    print(f"{y} is a leap year.")
    month_lengths["02"][2] = 29
elif 1 <= int(yeardict[0]) <= 12 and 1 <= int(yeardict[1]) <= 31:
     print(f"{y} is not a leap year.")
else:
    print(f"{year} is not a valid date.")
    valid = False

# I added this because it wasn't returning as an invalid date if the user typed something like 0/0/0. The program DOES still note whether the year is a leap year regardless.

if valid == True:
    if int(yeardict[0]) == 0 or int(yeardict[1]) == 0:
        print(f"{year} is not a valid date.")
        valid = False

# This is for if the user inputs a date that is higher than the bounds.

if valid == True:
    if int(yeardict[0]) > 12 and int(yeardict[1]) > 31:
        print(f"{y} is not a valid date.")
        valid = False

# Day of the week that January 1st falls on

yr = (y - 1)
day = int((36 + yr + (yr//4) - (yr//100) + (yr//400)) % 7)

for key, value in week_days.items():
    if day == value:
        dayname = key
        dayvalue = value

monthy = 0
for key, value in month_lengths.items():
    if int(yeardict[0]) == value[1]:
        # print(f"The month of the inputted date is {value[0]}.")
            # I used this to troubleshoot
        monthy = value[1]

# The inputted date's day number for the purposes of calculating the day of the week a date falls on

i = 1
summy = 0
for key, value in month_lengths.items():
    if value[1] < int(yeardict[0]):
        summy += value[2]

summy += int(yeardict[1])

# print(f"The day number of {year} is {summy}.")
    # I used this to troubleshoot when it came to leap years

# Noting what day of the week January 1 of that year falls on

if valid == True:
    print(f"January 1st occurs on a {dayname} in {yeardict[2]}.")

# Calculating the day of the week!

the_weekday = (int(dayvalue) + summy - 1) % 7

if valid == True:
    for key, value in week_days.items():
        if the_weekday == value:
            print(f"{year} is a {key}.")