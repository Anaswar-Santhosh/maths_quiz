import random
score = 0
#lists for history display
question_list = [] 
correct_answers = []
user_answers = []
#####################################################Instrucions##################################################################################
def show_instructions():
  while True:
    show_instructions = input(f'would you like to see the instrucions(yes,no) ').lower().strip()
    if show_instructions == 'yes':  
      print("""
============================= QUIZ INSTRUCTIONS ============================
You will be asked a question at a time.
Type your question and press enter.
If you got the answer correct it will show a massage and a ✅ mark.
If you answered it wrong, it will tell you it is incorrect and a ❌ mark.
For divition - the answer showed be round it up to 2 decimal point.
To skip a question enter 'skip' and press enter without typing anything.
You can choose the number of question from 15 to 30.
enter 999 to do infinite mode.
Type stop to quit infinite mode.
At the end you can choose to see the full history.
============================================================================
            """)
      break
    elif show_instructions == 'no':
      print('====================================================================')
      break
    else:
      print('Enter yes or no ')
###########################################check the year of the user is in side the range. ########################################################     
def year_level():
  while True:
    try:
      year_level = int(input('What year are you ( 1 to 8 ) '))

      if 1 <= year_level <= 8:
        print('====================================================================')
        return year_level
      elif year_level > 8:
        print('Sorry it only for year 1 to 8')
        print('====================================================================')
      else:
        print('Sorry, you are too young for this quiz')
        print('====================================================================')
    except ValueError:
      print()
      print("""
====================================================================     
Please enter a number
====================================================================
            """)
########################################################genarate the question print it and cheack if it right##################################################################  
def get_range_for_year_level(year_level):
  if year_level == 1:
    min_range = 1
    max_range = 10
    return min_range, max_range
  elif year_level == 2:
    min_range = 1
    max_range = 20
    return min_range, max_range
  elif year_level == 3:
    min_range = 1
    max_range = 50
    return min_range, max_range
  elif year_level == 4:
    min_range = 1
    max_range = 100
    return min_range, max_range
  elif year_level == 5:
    min_range = 1
    max_range = 100
    return min_range, max_range
  elif year_level == 6:
    min_range = 1
    max_range = 100
    return min_range, max_range
  elif year_level == 7:
    min_range = 1
    max_range = 1000
    return min_range, max_range
  elif year_level == 8:
    min_range = 1
    max_range = 10000
    return min_range, max_range
def generate_question(min_range, max_range):
  while True:
    first_number = random.randint(min_range, max_range)
    second_number = random.randint(min_range, max_range)
    operation_choices = ["+","-"]
    selected_operation = random.choice(operation_choices)  
    if selected_operation == "-" and first_number < second_number:
      continue
    else:
      break


  if selected_operation == "+":
    expected_answer = first_number + second_number

  elif selected_operation == "-":
    expected_answer = first_number - second_number

  question_list.append(f"What is {first_number} {selected_operation} {second_number}?")
  correct_answers.append(expected_answer)
  return expected_answer, selected_operation, first_number, second_number

def get_user_answer(question_data):
    skip_command = "skip"
    #printing question
    student_answer = input(f'What is {question_data[2]} {question_data[1]} {question_data[3]}? ').lower().strip()
    #answer checking - if user want to skiping and stop                 
    if student_answer == skip_command:
      student_answer = "skipped"     
      return student_answer 
    
    elif student_answer == "stop":
      return "stop"
    try:
      student_answer = int(student_answer)
      return student_answer
    except ValueError:
      print('Invalid! please enter a number')
      while True:
        try:
          student_answer = input(f"{question_list[-1]} ")
          if student_answer == skip_command:
            student_answer = "skipped"
            user_answers.append(student_answer)
            return student_answer    
          elif student_answer == "stop":
            return "stop"
          int(student_answer)
          break

        except ValueError:
          print('Invalid! please enter a number')
      return student_answer

def check_answer(expected_answer,student_answer):
    if student_answer == "skipped":
      user_answers.append(student_answer)
      print('You have skipped this question')
      return
    if student_answer == "stop":
      return

    #answer checking
    if student_answer == expected_answer:
      print('✅ Correct answer')
      global score
      score = score + 1
      user_answers.append(student_answer)  
      return 
    else:
      print('❌ Incorrect answer')
      user_answers.append(student_answer)

########################################################print the question deppenthing on the number of question need#######################################################################
def question_number(min_range, max_range): 
  min_questions = 15
  max_questions = 100
  infinite_code = 999
  questions_asked = 0

  while True:
    print(f'Pick a number of questions from {min_questions} to {max_questions}')
    print(f'For infinite mode enter {infinite_code}')

    question_count = input('How many questions would you like to be in this quiz ')

    try:
      if int(question_count) == infinite_code:
        print("==============================infinite mode=========================")
        while True:
          questions_asked = questions_asked + 1
          print(f'======question {questions_asked}======')
          question_data = generate_question(min_range, max_range)
          user_answer = get_user_answer(question_data)
          if user_answer == "stop" :
            break
          check_answer(question_data[0], user_answer)

        print("==========================end of infinite mode======================")
        history_display(questions_asked,question_count)  # calling history_display
        return 
      

      elif int(question_count) >= min_questions and int(question_count) <= max_questions:
        print('====================================================================')
        for i in range(int(question_count)):
          print(f'======question {i + 1}======')
          question_data = generate_question(min_range, max_range)
          user_answer = get_user_answer(question_data)
          check_answer(question_data[0], user_answer)  

        print('====================================================================')
        questions_asked = int(question_count)
        history_display(questions_asked,question_count)  # calling history_display    
        break


    except ValueError:
      print('====================================================================')


#######################################################
#history display
def history_display(questions_asked,question_count): 
  while True:
    view_history = input('Do you want to see your quiz history? ( Yes/No ) ').lower().strip()

    if view_history == "yes" and len(user_answers) == 0:
      print("You have quit before answering any questions")
      break

    elif view_history == "yes" and len(user_answers) > 0:
      for i in range(len(user_answers)):
        print(f"==============================Question {i+1}=============================")
        print (f"{question_list[i]}")

        if correct_answers[i] == user_answers[i]:
          print('You got the answer right! ✅')

        else:
          print('You got the answer wrong. ❌')
          print (f"Coreect answer was - {correct_answers[i]}")
        print (f"Your answer was - {user_answers[i]}")
      break


    elif view_history == "no":
      break

  int(score)
  int(questions_asked)
  print("=====================================================================") 
  if question_count == "999" and score > 0:
    print(f'You got {score} out of {questions_asked-1} in infinite mode') 
    score_percentage = round(score / (questions_asked-1) * 100)
  elif question_count != "999":
    print(f'You got {score} out of {questions_asked}')
    score_percentage  = round(score / questions_asked * 100)
  else:
    print(f'You got {score} out of {questions_asked}')
    print('Better luck next time')
    score_percentage = 0

  print(f'======={score_percentage}%======')

  feedback(score_percentage)
#######################################################
def feedback(score_percentage):
  if 90 <= score_percentage <= 100:
    print("Excellent work")
    print("Keep this good work up")
  elif 75 <= score_percentage <= 89:
    print("Good job, you're doing well")
    print("Keep this good work up")
  elif 60 <= score_percentage <= 74:
    print("Good effort")
    print("Keep this good work up")
  elif 40 <= score_percentage <= 59:
    print("You need some practice")
  elif 10 <= score_percentage <= 39:
    print("Needs more practice")
  else:
    print("need lot of practice but don't worry you can do it")
  print("=====================================================================") 
#######################################################
show_instructions()
user_year_level = year_level()
min_range, max_range = get_range_for_year_level(user_year_level)
question_number(min_range, max_range)
while True:
  play_again = input('Do you want do the quiz again ').lower().strip()
  if play_again == "yes":
    question_list.clear()
    correct_answers.clear()
    user_answers.clear()
    score = 0
    show_instructions()
    question_number(min_range, max_range)
  elif play_again == "no":
    print('Thank you for playing the quiz!')
    break
  else:
    print('Please enter yes or no')


