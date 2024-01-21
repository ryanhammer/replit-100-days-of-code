# Day 10 Challenge
myBill = float(input("What was the bill?: "))
tip = int(input("What % will you leave for tip?: "))
myBillWithTip = myBill * (1 + tip/100)
numberOfPeople = int(input("How many people?: "))
answer = myBillWithTip / numberOfPeople
print("You all owe", round(answer, 2))