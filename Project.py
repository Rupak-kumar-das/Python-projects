import random


user_choice = input('user pick rock,paper,scissor: ')
computer_choice=random.choice(['rock','paper','scissor'])
#print the input taken
print('user_choice=', user_choice)
print('computer_choice=',computer_choice)

# let's create logic
if user_choice=='rock' and computer_choice=='rock':
  print('draw')
elif user_choice=='rock' and computer_choice=='paper':
  print('computer won')
elif user_choice=='rock' and computer_choice=='scissor':
  print('user won')
elif user_choice=='paper' and computer_choice=='rock':
  print('user won')
elif user_choice=='paper' and computer_choice=='paper':
  print('draw')
elif user_choice=='paper' and computer_choice=='scissor':
  print('computer won')
elif user_choice=='scissor' and computer_choice=='rock':
  print('computer won')
elif user_choice=='scissor' and computer_choice=='paper':
  print('user won')
elif user_choice=='scissor' and computer_choice=='scissor':
  print('draw')
























'''
number1=5
number2=6

print(number1==5 and number2==6)
print(number1==3 and number2==6)
print(number1==5 and number2==4)
print(number1==3 and number2==8)

print(number1==5 or number2==6)
print(number1==3 or number2==6)
print(number1==5 or number2==4)
print(number1==3 or number2==8)
'''
