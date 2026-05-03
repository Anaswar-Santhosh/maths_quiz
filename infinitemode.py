#changing percentage for infinite
import random
from fractions import Fraction
def power ():
  #list of bases 
  base = [1 ,2 ,3 ,4 ,5 ,10 ]
  #list of powers 
  power = [1 ,2 ,3,4 ,10 ]
  while True:
    #try:
      rand_bese = random.choice(base)
      #pick a random power from the power list.
      rand_power = random.choice(power)
      right_ans = pow(rand_bese,rand_power)
      user_answer = int(input(f'{rand_bese} to the power of {rand_power}' ))
      if user_answer == right_ans:
        print(f"Great job the answer is {right_ans}")
        break
      else:
        print(f'opps you got it wrong the right answer was {right_ans}')
        print(f'You were close but the right answer was {right_ans}')
        break
    #day 2 15/03/2023
    #except:
      print("invalid")
      print("please ender Integer")
      print("")
      percentage()
      

def percentage ():
  while True:
    #try:
      random_percentage = random.randint(1, 99)
      number = random.randint(2500, 7000)
      answer = round(random_percentage / 100 * number)
      print(f" answer {answer}")
      user_answer = float(input(f"find {random_percentage}% percentage of {number}? "))
      if user_answer == answer:
        print("The answer is right!")
        power ()
      elif user_answer > 0 and user_answer < 7001:
        print(f"Nice try, The answer was {answer}")
        power ()
    #except:
      #print("invalid")
      #print("please ender Integer/Decimals")
      #print("")
      
percentage ()
      