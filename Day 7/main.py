# Challenge
print('Welcome to 76ers guess who!')

position = input('Guess the 76er! What position does he play? ')
if position == 'center':
  print('Figure out which center it is!')

  whichCenter = input('Which center had a lunatic previous coach proclaim there would not be a victory tour for you after you had a good game ? ')

  if whichCenter == 'Paul Reed':
    print('Congratulations! It IS Bball Paul Reed!')
  else:
    print("You are probably thinking of reigning NBA MVP Joel Embiid because who wouln't be? Unfortunately that is not the correct answer")
elif position == 'guard':
  guardWithPodcast = input('Name a guard who has a podcast: ')
  if guardWithPodcast == 'Tyrese Maxey':
    print('Congratulations! Tyrese Maxey DOES host a podcast!')
  elif guardWithPodcast == 'Pat Bev' or guardWithPodcast == 'PatBev' or guardWithPodcast == 'Patrick Beverley':
    print('Congratulations! Pat Bev DOES host a podcast!')
  else:
    print('Sorry, that is not one of the correct answers')
else:
  forwardWithCookies = input('Name the forward who has an ownership stake in a cookie company: ')
  if forwardWithCookies == "Tobias Harris":
    print('Correct! It is Tobias "Crumbl Cookies" Harris!')
  else:
    print('Sorry, that is wrong wrong wrong')