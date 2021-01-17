input=open('Input.txt','r').read().splitlines()
numbers={int(number[1]):int(number[0]) for number in enumerate(input[0].split(','))}
turn=0
t=len(numbers)+1
while t<2020:
   if turn in numbers:
      prevTurn=turn
      turn=t-numbers[turn]-1
      numbers[prevTurn]=t-1
   else:
      numbers[turn]=t-1
      turn=0
   t+=1
print(turn)