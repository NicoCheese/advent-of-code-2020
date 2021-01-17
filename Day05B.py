input=open('Input.txt','r').read().splitlines()
idList=[]
for boardPass in input:
   boardPass=boardPass.replace('F','0').replace('L','0').replace('B','1').replace('R','1')
   idList.append(int(boardPass[:7],2)*8+int(boardPass[7:],2))
idList.sort()
for index in range(len(idList)-1):
   if idList[index+1]-idList[index]==2:
      print(idList[index]+1)