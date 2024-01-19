# Tutorial
tvShow = input("What is your favorite tv show? ")
if tvShow == "The Office":
  print("Excellent choice?")
  faveCharacter = input("Who is your favorite character? ")
  if faveCharacter == "Dwight":
    print("You have never been cooler")
  else:
    print("It should be Dwight! Determined, Worker, Intense, Good Worker, Hard Worker, Terrific!")
elif tvShow == "Two and a Half Men":
  print("Woof")
else:
  print("Yeah, that's cool and all…")

# Common Errors
tvShow = input("What is your favourite tv show? ")
if tvShow == "peppa pig":
  print("Ugh, why?")
  faveCharacter = input("Who is your favourite character? ")
  if faveCharacter == "daddy pig":
    print("Right answer")
  else:
    print("Nah, Daddy Pig's the greatest")
elif tvShow == "paw patrol":
  print("Aww, sad times")
else:
  print("Yeah, that's cool and all…")

# Fix My Code
order = input("What would you like to order: pizza or hamburger? ")
if order == 'hamburger':
  print("Thank you.")

  cheese = input("Do you want cheese? ")

  if cheese == 'yes':
    print("You got it.")
  else: 
    print("No cheese it is.")

elif order == 'pizza':
  print("Pizza coming up.")

  toppings = input("Do you want pepperoni on that? ")

  if toppings == "yes":
    print("We will add pepperoni.")
  else:
    print("Your pizza will not have pepperoni.")