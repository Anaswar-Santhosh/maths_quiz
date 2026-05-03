#day one 13/3/2026
import random


def percentage ():
  while True:
    try:
      random_percentage = random.randint(1, 99)
      number = random.randint(2500, 7000)
      answer = round(random_percentage / 100 * number)
      print(f" answer {answer}")
      user_answer = float(input(f"find {random_percentage}% percentage of {number}? "))
      if user_answer == answer:
        print("The answer is right!")
        break
      elif user_answer > 0 and user_answer < 7001:
        print(f"Nice try, The answer was {answer}")
        break
    except:
      print("invalid")
      print("please ender Integer/Decimals")
  
print("moving on")  
  
  
percentage()