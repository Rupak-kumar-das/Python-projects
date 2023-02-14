print('rupak')
#for printing interior and float
print(22,78.9,end='.')
#variable
name='rupak'
number=25.4
print(name,number)
print(type(name),type(number))
#input (The below text should be unhidden during understanding)
#x=input('Enter your name- ')
#print(x)
# Conditioning
age = 27
if age < 25:
  print('Age is less than 25')
elif age>25:
  print('age is greater than 25')
else:
  print('he is not born')
#Calculator
operand1=input('please enter number1- ')
operand2=input('please enter number2- ')
# The result of input always will be string. So converting string into interior
operand1=int(operand1)
operand2=int(operand2)
result=operand1+operand2
print('the result is: ',result)

  