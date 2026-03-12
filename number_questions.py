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