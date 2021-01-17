input=open('Input.txt','r').read().splitlines()
count=0
group=''
for line in input:
   if line:
      group+=line
   else:
      count+=len(set(group))
      group=''
print(count+len(set(group)))