print('\033[1;33mHIGH SCORE TABLE\033[0m')
a = open('high.score', 'a+')
while True:
  print()
  ask = input('Input your Initials and your Score(Out of 100,000). Seperate them with a space: ').split()
  a.write(f'{ask[0]} {ask[1]}\n')
  print()
  response = input('Want to add again? y/n: ') 
  if response == 'y':
    continue 
  else:
    break 
a.close()