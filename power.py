import random
right_answer = "Great job the answer is right"
wrong_answer = "nice try but the a answer was"

def Power ():
  Positive_no = [2 , 3, 4, 5 , 5 , 10]
  power = [2 ,3 ,4 ]
  while True:
    try:
      #Positive_no santand for positove number
      # get random power and the number
      rand_power = random.choice(power)
      rand_no = random.choice(Positive_no)
      r_answer = pow(rand_no,rand_power)
      user_answer = int(input(f"Calculate: {rand_no}^{rand_power} "))
      if user_answer == r_answer:
        print(right_answer)
        break
      else:
        print(f'{wrong_answer} {r_answer}')
        break
    except:
      print("invalid")
      print("")
Power()
