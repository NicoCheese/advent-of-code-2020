from collections import deque

input=open('Input.txt','r').read().splitlines()
cups=deque([int(i) for i in input[0]])
cupLength=len(cups)
pickedLength=3
cups.rotate(len(cups)-pickedLength-1)
t=0
while t<100:
   current=cups[-4]
   picked=[]
   for i in range(pickedLength):
      picked.append(cups.pop())
   picked=picked[::-1]
   destination=current-1
   while destination in picked or destination<1:
      destination-=1
      if destination<1:
         if cupLength not in picked:
            destination=cupLength
         elif cupLength-1 not in picked:
            destination=cupLength-1
         elif cupLength-2 not in picked:
            destination=cupLength-2
         else:
            destination=cupLength-3
   rot=cupLength-pickedLength-cups.index(destination)-1
   cups.rotate(rot)
   cups.extend(picked)
   cups.rotate(-rot-pickedLength-1)
   t+=1
cups=list(cups)
target=cups.index(1)
output=''
for cup in cups[target+1:]+cups[:target]:
   output+=str(cup)
print(output)