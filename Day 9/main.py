# Day 9 Challenge
birthYear = int(input("What year were you born? "))

if birthYear >= 1925 and birthYear <= 1946:
  print("You are a Traditionalist.")
elif birthYear >= 1947 and birthYear <= 1964:
  print("You are a Baby Boomer.")
elif birthYear >= 1965 and birthYear <= 1981:
  print("You are a Generation X member.")
elif birthYear >= 1982 and birthYear <= 1995:
  print("You are a Millenial.")
elif birthYear >= 1996 and birthYear <= 2015:
  print("You are a Generation Z member (and you suck).")
else:
  print("You are either too old or too young to be on this list.")