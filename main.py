import random


def Percentages ():
  while True:
    try:
      Percentages = random.randint(1, 99)
      percentages_of = random.randint(300, 5000)
      print('make sure to round it up to 2.d.p')
      answer = round(Percentages / 100 * percentages_of)
      print(f'testing purpose {answer}')
      user_input = float(input(f'what is {Percentages}% of {percentages_of} '))
      if user_input == answer:
        print("🎉 Great job! You got the answer right!")
        break
      elif user_input > 0 and user_input < 5001:
        print(f'f"😅 Nice try! ❌ The correct answer was {answer}! 🎯✨')
        break
    except:
      print("integer and float only")
      print("")
      
      
      
#Positive whole numbers as bases: 2, 3, 4, 5, 10, etc.

#Small exponents: usually 2, 3, 4, sometimes 5 or 6

#Negative numbers as bases: often with small powers, like −2², (−3)³

def Power ():
  Positive_no = [2 , 3, 4, 5 , 5 , 10]
  power = [2 ,3 ,4 ]
  while True:
    try:
      #Positive_no santand for positove number
      # get random power and the number
      rand_power = random.choice(power)
      rand_no = random.choice(Positive_no)
      r_answer =pow(rand_no,rand_no)
      print(r_answer)
      user_answer = input(f"Calculate: {rand_no}^{rand_power} ")
      if r_answer == user_answer:
        print("🎉 Great job! You got the answer right!")
        break
      elif user_answer != r_answer:
        print(f'f"😅 Nice try! ❌ The correct answer was {r_answer}! ')
        break
    except:
      print("invalid")
      print("")


 #instructions 
while True:
  try:
    #asking if thay want to see the instruction
    Instructions = input (f' would you like to see the Instreuction (yes, no) ').lower()
    if Instructions == 'yes': # the instrutions
      print('=======Instructions=======')
      print('I will ask you one question at a time.')
      print('You answer in the chat.')
      print('If your answer is correct it will tell you.')
      print('If it’s wrong, it wil show you the right answer')
      print('The question and answer would be given at the end')
      break
    elif Instructions == 'no':
      break
    # if that type anything else, asking them agin
    else:
      print('Enter yes or no ')
  except:
    print('Enter yes or no ')
print('')
      
      
#asking how may questions do that want
while True:
  try:
    # asking how may questions do that want
    print('👉 Pick a number between 15 and 30')
    questions= int(input('How many questions do you want for your quiz? '))
    # checking it's between the range
    if 14 < questions and 31 > questions:
      break
    # leves a blenk line to and the code would repite 
    else:
      print('')
  except:
    print('')

print('')


# asking if you want to start or no 
while True:
  try:
    # asking if you want to start or no
    start_yes_no = input ('do you like to start the quiz? ').lower()
    # checking 
    if start_yes_no == 'yes':
      print('starting quiz')
      break
    elif start_yes_no == 'no':
      print('Tell me whan your ready')
    # types something else ask them to type yes or no
    else:
      print('Enter yes or no ')
  except:
    print('Enter yes or no ')

