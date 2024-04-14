def login():
  while True:
    username = input('What is your username > ')
    password = input('What is your password > ')
    if username == 'nina' and password == 'pass':
      print('Welcome!')
      break
    else:
      print("That's not correct. Please try again...")
      continue

print('THE REPLIT LOGIN SYSTEM')
print()
login()