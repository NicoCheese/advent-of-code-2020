input=open('Input.txt','r').read().splitlines()
x=0
y=0
targetX=10
targetY=1
for command in input:
   if command[0]=='N':
      targetY+=int(command[1:])
   elif command[0]=='S':
      targetY-=int(command[1:])
   elif command[0]=='E':
      targetX+=int(command[1:])
   elif command[0]=='W':
      targetX-=int(command[1:])
   elif command[0]=='L':
      for i in range(int(command[1:])//90):
         originalX=targetX
         targetX=-targetY
         targetY=originalX
   elif command[0]=='R':
      for i in range(int(command[1:])//90):
         originalX=targetX
         targetX=targetY
         targetY=-originalX
   else:
      x+=int(command[1:])*targetX
      y+=int(command[1:])*targetY
print(abs(x)+abs(y))