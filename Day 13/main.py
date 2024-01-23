# Day 13 Challenge
print("Welcome to the Grade Generator")
testName = input("What is the name of the test? ")
maxScore = int(input("What is the maximum score you could receive? "))
yourScore = int(input("What is the score you received? "))
percentage = round(yourScore / maxScore * 100, 2)

if percentage >= 90:
  print("You got", percentage, "% which is an A+ on the", testName, "test")
elif percentage >= 80:
  print("You got", percentage, "% which is an A on the", testName, "test")
elif percentage >= 70:
  print("You got", percentage, "% which is a B on the", testName, "test")
elif percentage >= 60:
  print("You got", percentage, "% which is a C on the", testName, "test")
elif percentage >= 50:
  print("You got", percentage, "% which is a D on the", testName, "test")
elif percentage < 50:
  print("You got", percentage, "% which is a U on the", testName, "test")