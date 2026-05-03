#probability
from fractions import Fraction
import random
even = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50,60,70,80,]
#day 6 19/03/2026 
while True:
  try:
    random_even = random.choice(even)
    print(f'A bag has {random_even} marbles')
    red = round(20 / 100 * random_even)
    blue = round(12 / 100 * random_even)
    green = round(8 / 100 * random_even)
    yellow = round(60 / 100 * random_even)
    print(f"There are {red} red marbles")
    print(f"There are {blue} blue marbles")
    print(f"There are {yellow} yellow marbles")
    print(f"There are {green} green marbles")
    answer = Fraction(green,random_even)
    print(f'answer = {answer}')
    print(f'Jack pick one marble from the back what is the probability of getting green in a fraction ')
    print('write in the simplify the fraction')
    user_answer = input('what is the probability of getting green? (write it like this 1/2) ')
    #day six 20/03/2026
    if user_answer == answer:
      print("correct answer")
      break
      
    else:
      print("wrong answer")
      print('')
      break
      
  except:
    print('Invalid')
    print('')