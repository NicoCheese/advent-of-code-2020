input=open('Input.txt','r').read().splitlines()
input.append('')
count=0
group=''
groupSize=0
for line in input:
   if groupSize==0:
      firstPerson=line
   if line:
      group+=line
      groupSize+=1
   else:
      for char in firstPerson:
         if group.count(char)==groupSize:
            count+=1
      group=''
      groupSize=0
print(count)