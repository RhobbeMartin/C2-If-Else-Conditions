a = 200
b = 33

if (b > a): 
  print("b is greater than a")
else:
  print("b is not greater than a")

# Write a conditional statement that evaluates if the user input is positive or negative

a = 5000 
num = int(input("Enter a number:"))
if(num > 0):
  print("I see that your number is positive")
elif(num == 0):
  print("You have entered 0")
else:
  print("It's negative")

# Ask the user for their age
#If they are younger than 13 and older 13, tell them they can only watch PG/G movies
#If they are 13 and older but younger than 17, They can only watch PG-13/PG/G movies
# If they are 17 and older, They can watchall the movies

age = int(input("what is your age?"))
if(age < 13):
 print("you can only PG/G movies")
elif(17> age >= 13):
  print("That means you can watch PG-13 and PG/G movies")
else:
  print("You can watch all movies")

is_Hungry = False
is_Sleepy = False
if(is_Hungry == True):
  print("You should go eat")
if(is_Sleepy == True):
  print("You should go sleep")
if(is_Sleepy == False):
  print("wow you're well rested")

userNum = int(input("Choose a number:"))

if(userNum % 2 != 0):
  print( "Your number is odd")
else: 
  print("Your numbert is even")

#Math Quadtrants

# Ask the user for an x and a y value

# using a nested conditional, output which quadrant they are in
x = int(input("please give me an x value:"))
y = int(input("please give me an y value:"))


if(x > 0):
 if(y > 0):
   print("Your number is in the first quardrant")
  else:
    print(" Your number is at the forth quadrant")
elif(x < 0):
  if(y < 0):
    print("Your number is in the third quadrant")
  if(y > 0):
    print("Your number is in the second quadrant")

if(x == 0):
    if(y == 0):

      print("You are on the origin")