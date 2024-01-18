print('Welcome to your adventure simulator. I am going to ask you a bunch of questions and then create an epic story with you as the star!')

name = input('What is your name? ')
enemy = input('Enter a good name for the villain of the story: ')
hasSuperpower = input('Do you have a superpower? Enter "yes" or "no": ').lower()

if hasSuperpower == 'yes': superpower = input('What is your superpower? ')
else: superpower = 'deftly reason nonviolently with even the most uncivilized people'

location = input('Where do you live? ')
knownAssociates = input('Who are some of your best friends? ')
vehicle = input('What is your adventure vehicle? For example, Batman had the Batmobile. What is your version of the Batmobile? ')

print('Hello', name + '! Your ability to', superpower, 'will make sure you never have to look at', enemy + '’s face again. You will be able to cruise down the streets of', location, 'with', knownAssociates, 'in your', vehicle, 'and', superpower, 'for the power of good and not evil!')