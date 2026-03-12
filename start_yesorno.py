while True:
  try:
    # asking if you want to start or no
    start_yes_no = input ('do you like to start the quiz? ').lower()
    # checking 
    if start_yes_no == 'yes':
      print("")
      break
    elif start_yes_no == 'no':
      print('Tell me whan your ready')
    # types something else ask them to type yes or no
    else:
      print('Enter yes or no ')
  except:
    print('Enter yes or no ')