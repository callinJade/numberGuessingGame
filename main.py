#import library
import random

#print('Hello World')
#print('My name is: Jade')
print("Number Guessing Game!")

number = random.randint(1,25) 
chances = 0 #counter
maxChances = 5 #total number of chances you get each game

print("Guess a number between 1 and 25!")

while (chances < maxChances):
  guess = int(input())
  if guess == number:
    print("Congradualtions, you won!!")
    break
  elif guess < number:
    print("Your guess was too low. Guess a larger number")
    chances += 1
  else:
    print("Your guess was too high. Try a smaller number")
    chances += 1

  if chances >= maxChances:
    print("You lose!! The number is", number)