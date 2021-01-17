input=open('Input.txt','r').read().splitlines()
buses=[int(id) for id in input[1].replace('x','1').split(',')]
t=0
skip=1
depth=0
found=False
while not found:
   found=True
   t+=skip
   for bus in enumerate(buses):
      if (t+bus[0])/bus[1]%1!=0:
         found=False
         break
      elif bus[0]>=depth:
         depth+=1
         skip*=bus[1]
print(t)