user = True
while (user == True):
  print("welocome to kon banega lakhpati\n\
\n")
  que = [
      '''who is the prime minister of india?''',
      '''who is the president of india?''',
      '''who is the chief minister of india?'''
  ]
  ans = [
      '''1)Droupadi Murmu''', '''2)ram nath kovind''', '''3)APJ abdul kalam'''
  ]
  print(que[1],"\n")
  print("you are option is", ans,"\n", sep="\n")
  a = int(input('''enter the option number: '''))
  if (a == 2):
    print('''corremt answer ''')
    print('''you gotted rs.1000''')
  else:
    print('''wrong answer''')
    print('''you out through the game''')
    user = False
    break

  print("\n\n")
  print(que[0])
  print("you are option is", ans, sep="\n")
  b = int(input('''enter the option number: '''))
  if (b == 1):
    print('''corremt answer ''')
    print('''you gotted rs.10000''')
  else:
    print('''wrong answer''')
    print('''you out through the game''')
    user = False
    break
  print("\n\n")
  print(que[2])
  print("you are option is", ans, sep="\n")
  c = int(input('''enter the option number: '''))
  if (c == 3):
    print('''corremt answer ''')
    print('''you gotted rs.1000000''')
    user = False
    break

  else:
    print('''wrong answer''')
    print('''you out through the game''')
    user = False
    break

print("thank you for playing")
  
