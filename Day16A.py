import re

input=open('Input.txt','r').read().splitlines()
rangeSet=set()
for line in input:
   if not line:
      break
   numbers=[int(i) for i in re.findall('\d+',line)]
   rangeSet.add((range(numbers[0],numbers[1]+1),range(numbers[2],numbers[3]+1)))
tickets=set()
for line in input[::-1]:
   if line=='nearby tickets:':
      break
   tickets.add(tuple([int(i) for i in line.split(',')]))
errorRate=0
for ticket in tickets:
   for field in ticket:
      invalid=True
      for ranges in rangeSet:
         if field in ranges[0] or field in ranges[1]:
            invalid=False
            break
      if invalid:
         errorRate+=field
print(errorRate)