# Challenge
print('Welcome to 76ers guess who!')

isCenter = input('Are you a rim protector (enter "yes" or "no")? ')
if isCenter == 'yes':
  print('You might be Joel Embiid!')

  hadVictoryTour = input('Have you ever had a lunatic previous coach proclaim there would not be a victory tour for you after you had a good game (enter "yes" or "no")? ')

  if hadVictoryTour == 'yes':
    print('You are Bball Paul Reed!')
  else:
    hadSongNamed = input('Have you ever had a song named after you (enter "yes" or "no")? ')
    if hadSongNamed == 'yes':
      print('You are Mo Bamba!')
    else:
      print('You are reigning NBA MVP Joel Embiid!')
else:
  isGuard = input('Are you a lead ballhandler (enter "yes" or "no")? ')
  if isGuard == 'yes':
    hasPodcast = input('Have you ever had a podcast named after you (enter "yes" or "no")? ')
    if hasPodcast == 'yes':
      isPatBevPod = input('Do you cohost a podcast with a guy named Rone (enter "yes" or "no")? ')
      if isPatBevPod == 'yes':
        print('You are Patrick Beverly!')
      else:
        print('You are Tyrese Maxey!')
    else:
      print('You are DeAnthony Melton!')
  else:
    print('You are Tobias Harris probably')
