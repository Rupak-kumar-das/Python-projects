'''
password='8638'
Trials=3

while True:
  
  user_password=input('please enter your password: ')
  if password != user_password:
    Trials-=1
    if Trials==0:
      print('you not have trial')
      break
    print('wrong password',Trials,'trial left')

  else:
    print('welcome')
    break
'''
from time import sleep
password='8638'
Trials=3

while True:
  
  user_password=input('please enter your password: ')
  if password != user_password:
    Trials-=1
    if Trials==0:
      counting=5
      while True:
        print('phone is locked for',counting,'seconds')
        counting-=1
      
        if counting==0:
          Trials=3
          break
        sleep(1)
    print('wrong password',Trials,'trial left')

  else:
    print('welcome')
    break
