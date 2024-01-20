# Day 8 Challenge
print('DAILY AFFIRMATION GENERATOR')

name = input('What is your name? ')
day = input('What day of the week is it? ')

strengthOne = input('What is your greatest strength? ')
strengthTwo = input('What is your second greatest strength? ')
favoriteLunch = input('What is your favorite thing to have for lunch? ')
weeklyGoal = input('What goal would you like to set for yourself this week? ')
favoriteHobby = input('What is your favorite hobby? ')

if day == 'Monday' or day == 'monday':
  print('Happy Monday', name + '!', "It's the start of the week, but you're stronger than you think. Celebrate your ability to", strengthOne, "and start working toward achieving your goal of", weeklyGoal + '.')
elif day == 'Tuesday' or day == 'tuesday':
  print('Good Morning', name + '!', "You're stronger than you think. On this fine Tuesday, celebrate your knack for", strengthTwo, "and keep working toward that goal of", weeklyGoal + '.')
elif day == 'Wednesday' or day == 'wednesday':
  print('Hi', name + '!', "It's hump day! Remember, after today it's all downhill for the rest of the week. Help get yourself through the day by eating", favoriteLunch + '.', "Remember...you got this!")
elif day == 'Thursday' or day == 'thursday':
  print('Hey', name + '!', "It's Thursday, and you're over the hump!", "Keep working toward that goal of", weeklyGoal + '.', "Let's use two of your strenths today,", strengthOne, "and", strengthTwo + ',', "to work toward (and maybe even achieve) that goal of", weeklyGoal + '.')
elif day == 'Friday' or day == 'friday':
  print('Woohoo', name + '!', "It's Friday, and you're almost done with the week! Let's finish off that goal of", weeklyGoal, "if you haven't already.", "Then we can start planning out a weekend full of", favoriteHobby + '.')
else:
  print("Woot woot! It's the weekend! Relax and enjoy your day off", name + '!')