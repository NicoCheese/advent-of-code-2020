input=open('Input.txt','r').read().splitlines()
max=0
for boardPass in input:
   boardPass=boardPass.replace('F','0').replace('L','0').replace('B','1').replace('R','1')
   id=int(boardPass[:7],2)*8+int(boardPass[7:],2)
   if id>max:
      max=id
print(max)