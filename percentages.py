import random
right_answer = "Great job the answer is right"
wrong_answer = "nice try but the a answer was "

def Percentages ():
  while True:
    try:
      Percentages = random.randint(1, 99)
      percentages_of = random.randint(300, 5000)
      print('make sure to round it up to 2.d.p')
      answar = round(Percentages / 100 * percentages_of)
      user_input = float(input(f'what is {Percentages}% of {percentages_of} '))
      if user_input == answar:
        print(right_answer)
        break
      elif user_input > 0 and user_input < 5001:
        print(f"{wrong_answer} {answar}")
        break
    except:
      print("integer and float only")
      print("")