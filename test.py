# random library to use random
import random
correct_answer_count = 0
questions = []
right_answer = []
user_input = []
#####################################################Instrucions##################################################################################
# defining instructions
def instructions():
  #loop if thay type something other then yes or no
  while True:
    #asking for permission for instructions
    instructions = input(f'would you like to see the instrucions(yes,no) ').lower().strip()
    #checking if user input is yes
    if instructions == 'yes':
      #printing the Instrucions
      print('========================= QUIZ INSTRUCTIONS ========================')
      print(f'You will be asked a question at a time.')
      print(f'Type your question and press enter.')
      print(f'If you got the answer correct it will show a massage and a ✅ mark.')
      print(f'If you answered it wrong, the right answer would be shown.') 
      print(f'For divition - the answer showed be round it up to 2 decimal point.')
      print(f'To skip a question press enter without typing anyting.')
      print(f'You can choose the number of question from 15 to 30.')
      print(f'enter 999 to do infinite mode.')
      print(f'Type stop to quit infinite mode.')
      print('At the end you can choose to see the full history.')
      print('====================================================================')
      break
    #checking if user input is no
    elif instructions == 'no':
      print('====================================================================')
      break
    # if that type anything else, asking them again
    else:
      print('Enter yes or no ')
#########################To skip a question press enter without typing anyting##################check the year of the user is in side the range. ########################################################     
#defining a function called age_group
def age_group():
  #loop if thay type something other then the year range
  while True:
    #aking there year
    year = input('what year are you ( 1 to 8 ) ').strip()
    #years that qualify
    years = ["1","2","3","4","5","6","7","8",]
    #chacking if the user input is inside the age range 
    if year in years:
      print('====================================================================')
      # returing it so we can use the year out side the def age_group
      return year
    # if that type something out side the range 
    else:
      print('====================================================================')
      print('Enter a year between 1 to 8 ')
      
###################################################################################################################################################  
#defining a function called questiom_genrater
def questiom_genrater(year):
  try:
    #check if year is 1 or 2 
    if year == '1' or year == '2':
      #genrate random numbers 
      num1 = random.randint(1,9)
      num2 = random.randint(10,19)
      #list the symbol
      question_type = ["+","-"]
      #choice a random symbol from the question_type list
      choice  = random.choice(question_type)
      
    #check if year is 3 or 4
    elif year == "3" or year == '4':
      #genrate random numbers 
      num1 = random.randint(1,20)
      num2 = random.randint(1,50)
      num3 = random.randint(1,10)
      num4 = random.randint(1,10)
      #list the symbol
      question_type = ["+","-","*","/"]
      #choice a random symbol from the question_type list
      choice  = random.choice(question_type)
                              
    #check if year is 5 or 6
    elif year == "5" or year == '6':
      #genrate random numbers 
      num1 = random.randint(50,250)
      num2 = random.randint(10,100)
      num3 = random.randint(1,12)
      num4 = random.randint(1,12)
      #list the symbol
      question_type = ["+","-","*","/"]
      #choice a random symbol from the question_type list
      choice  = random.choice(question_type)
                              
                              
    #check if year is 7 or 8
    elif year == '7' or year == '8':
      #genrate random numbers 
      num1 = random.randint(50,500)
      num2 = random.randint(30,100)
      num3 = random.randint(1,20)
      num4 = random.randint(2,20)
      #list the symbol
      question_type = ["+","-","*","/"]
      #choice a random symbol from the question_type list
      choice  = random.choice(question_type)
      
      #checking if the choice = +
    if choice == "+":
      #finding the answer 
      correct_answer = num2 + num1 
      questions.append(f"What is {num2} {choice} {num1}?")
    #checking if the choice = -
    elif choice == "-":
      #finding the answer 
      correct_answer = num2 - num1
      questions.append(f"What is {num2} {choice} {num1}?")
    #checking if the choice = *
    elif choice == "*":
      #finding the answer 
      correct_answer = num3 * num4
      questions.append(f"What is {num3} {choice} {num4}?")
    #checking if the choice = /
    elif choice == "/":
      # round the answer to 2 dp and find the answer 
      correct_answer =round( num3 / num4 , 2)
      # tall the user to round the answer to 2 dp if needed
      print ('Make sure to round it up to 2 decimal point')
      questions.append(f"What is {num3} {choice} {num4}?")#@@@@@@@@@@@@
      
    
    #printing the question 
    if choice in ["+","-"]:
      user_answer = input(f'what is {num2} {choice} {num1} ').lower().strip()
    else:
      user_answer = input(f'what is {num3} {choice} {num4} ').lower().strip()
    right_answer.append(correct_answer)#@@@@@@@@@@@@
  
  # when user enter nothing it privent it from printing "'Invalid! please enter a number"
    if user_answer == "":
      user_answer = "Not answered"
      print(f'The correct answer is {correct_answer}')
      user_input.append(user_answer)#@@@@@@@@@@@@@
      return 
    elif user_answer == "stop":
      return "stop"
    
    try:
      if "." in user_answer:
        user_answer = float(user_answer)
      else:
        user_answer = int(user_answer)
      
    except ValueError:
      print('Invalid! please enter a number')
      return 
    
    #cheaking user input is correct or incorrect and talling them
    if user_answer == correct_answer:
      print('✅ Correct answer')
      global correct_answer_count
      correct_answer_count = correct_answer_count + 1
      user_input.append(user_answer)
      return 
    else:
      print('❌ Incorrect answer')
      print(f'The correct answer is {correct_answer}')
      user_input.append(user_answer)
  #privent them from tryping invalid number
  except ValueError:
    print('Invalid!')
  # returing year so year can be used out side this def 
   
  
     
###################################################################################################################################################
# defining a function called question_number and used the return year
def question_number(year):
  variable = 0
  while True:
    print('Pick a number of questions from 15 to 30')
    print('For infinite mode enter 999')
    try:
      num_questions = int(input('How many questions would you like to be in this quiz '))
    except ValueError:
      print('Pick a number of questions from 15 to 30')
      print('For infinite mode enter 999')
    if num_questions == 999:
      print("==============================infinite mode=========================")
      variable = 0
      while True:
        variable = variable + 1
        print(f'======question {variable}======')
        collect = questiom_genrater(year)
        if collect == "stop" :
          break
    
        
      print("==========================end of infinite mode======================")
      histery_print()
      return 
        
    elif num_questions > 14 and num_questions < 30:
      print('====================================================================')
      for variable in range(num_questions):
        print(f'======question {variable + 1}======')
        questiom_genrater(year)
      print('====================================================================')
      print(f'You got {correct_answer_count} out of {num_questions}')
      histery_print()
      break

    else:
      print('Enter a number between 15 and 30')
#############################print("=========infinite mode==================================================================")################################################################################################
def infinite_mode(year):
  correct_answer_count = 0
  variable = -1
  correct_answer_count =0
  while True:#loop
    variable = variable + 1
    if year == '1' or year == '2':
      num1 = random.randint(1,10)
      num2 = random.randint(1,10)
      question_type = ["+","-"]
      choice  = random.choice(question_type)
    elif year == "3" or year == '4':
      num1 = random.randint(1,20)
      num2 = random.randint(1,50)
      num3 = random.randint(1,10)
      num4 = random.randint(1,10)
      question_type = ["+","-","*","/"]
      choice  = random.choice(question_type)
    elif year == '5' or year == '6':
      num1 = random.randint(50,250)
      num2 = random.randint(10,100)
      num3 = random.randint(1,12)
      num4 = random.randint(1,12)
      question_type = ["+","-","*","/"]
      choice  = random.choice(question_type)
    elif year == '7' or year == '8':
      num1 = random.randint(50,500)
      num2 = random.randint(30,100)
      num3 = random.randint(1,20)
      num4 = random.randint(2,20)
      question_type = ["+","-","*","/"]
      choice  = random.choice(question_type)

    if choice == "+":
      correct_answer = num2 + num1 
      questions.append(f"What is {num2} {choice} {num1}?")
    elif choice == "-":
      correct_answer = num2 - num1
      questions.append(f"What is {num2} {choice} {num1}?")
    elif choice == "*":
      correct_answer = num3 * num4
      questions.append(f"What is {num3} {choice} {num4}?")
    elif choice == "/":
      correct_answer =round( num3 / num4 , 2)
      print ('Make sure to round it up to 2 decimal point')
      questions.append(f"What is {num3} {choice} {num4}?")

    right_answer.append(correct_answer)
    
    if choice in ["+","-"]:
      print(f'======question {variable + 1}======')
      user_answer = input(f"What is {num2} {choice} {num1}? ").strip()
    else:
      print(f'======question {variable + 1}======')
      user_answer = input(f"What is {num3} {choice} {num4}? ").strip()
    if user_answer == "":
      break
    try:
      if "." in user_answer:
        user_answer = float(user_answer)
      else:
        user_answer = int(user_answer)
    except ValueError:
      print('Invalid! please enter a number')
      return 
      
    
    #cheaking user input is correct or incorrect and talling them
    if user_answer == correct_answer:
      print('✅ Correct answer')
      correct_answer_count = correct_answer_count + 1
      user_input.append(user_answer)
    else:
      print('❌ Incorrect answer')
      print(f'The correct answer is {correct_answer}')
      user_input.append(user_answer)
  #privent them from tryping invalid number
 

#######################################################
def histery_print(): 
  show_history = input('Do you want to see your quiz history? ( Yes/No ) ').lower().strip()
  if show_history == "yes":
    if len(user_input) == 0:
      print("You have quit before answering any questions")
    for i in range(len(user_input)):
      print(f"==============================Question {i+1}=============================")
      print (f"{questions[i]}")
      if right_answer[i] == user_input[i]:
        print('You got the answer right! ✅')
      else:
        print('You got the answer wrong. ❌')
        print (f"Coreect answer was - {right_answer[i]}")
      print (f"Your answer was - {user_input[i]}")

    print("=====================================================================")     


#######################################################
#calling the functions 
instructions()
year = age_group()
question_number(year)

