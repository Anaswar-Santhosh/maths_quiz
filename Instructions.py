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
      