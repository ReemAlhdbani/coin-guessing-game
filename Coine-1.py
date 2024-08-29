

import random
print("welcom to coin guessing game !")
print("choice a method to ross the coin :\n1- Using random.randint()\n2- Using random.random()")

user_choice= int(input("Enter your choice (1 or 2 ) : "))
# Check the user's choice and determine the computer's result
if user_choice == 1:
    ron=random.randint(0,1)
    if ron == 0:
     computer_result= "tails"
    else: 
     computer_result= "heads"
elif user_choice == 2:
   ron2=random.random()
   if ron2 > 0.5:
      computer_result = "heads"
   else:
      computer_result = "tails"
else:
     print("Inviled choices...")
# Get the user's guess
choice2= input("Enter your guess tails or heads : ").lower()
# Check if the user's guess matches the computer's result
if choice2.lower() == computer_result.lower():
   print("Congrat you win !> - <")
else:
   print("tray agine... ")

print(f"the result of cmputer was {computer_result}")  
