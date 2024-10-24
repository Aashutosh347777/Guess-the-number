import random

max_num = input('Till what you want to guess a number: ')
if max_num.isdigit():
  max_num = int(max_num)
  if max_num <= 0:
    print('Enter a number greater than zero next time.')
    quit()
else:
  print('Please enter a number on next attempt.')
  quit()
random_number = random.randint(0,max_num)

guesses = 0
while True:
  guesses += 1
  user_guess = input('Make a guess: ')
  if user_guess.isdigit():
    user_guess = int(user_guess)
  else:
    print('Enter a number next time.')
    continue

  if user_guess == random_number:
    print('OHHH you got it.')
    break
  elif user_guess < random_number:
    print('You were below the number.')
  else:
    print('You were above the number.')


print(f'You got it in {guesses} times')