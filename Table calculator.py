from time import sleep
number=input('which table should we calculate: ')
multiplier=input('To which should we calculate: ')
print(number,'is the table we calculating to',multiplier)
number=int(number)
multiplier=int(multiplier)
value=1

while True:
  print(number,"x",value,"=",number*value)
  sleep(1)
  if value==multiplier:
     break
  value+=1  