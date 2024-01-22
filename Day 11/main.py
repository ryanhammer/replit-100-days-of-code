# Day 11 Challenge
print('Welcome to the Seconds Per Year calculator!')

secondsPerMinute = 60
minutesPerHour = 60
hoursPerDay = 24
isLeapYear = input("Is it a leap year? (Yes or No) ")

if isLeapYear == "Yes" or isLeapYear == "Y" or isLeapYear == "yes":
  daysPerYear = 366
else:
  daysPerYear = 365

secondsPerYear = secondsPerMinute * minutesPerHour * hoursPerDay * daysPerYear
print("There are", secondsPerYear, "seconds in a", "leap" if isLeapYear else "", "year.")