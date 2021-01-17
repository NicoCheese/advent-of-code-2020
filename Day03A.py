input=open('Input.txt','r').read().splitlines()
x=0
count=0
for y in input:
   if y[x]=='#':
      count+=1
   x=(x+3)%len(input[0])
print(count)