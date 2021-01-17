input=open('Input.txt','r').read().splitlines()
input=[int(i) for i in input[0]]
add=[i+len(input)+1 for i in range(1000000-len(input))]
input=input+add
input=[i-1 for i in input]
cups=[0 for i in range(len(input))]
for i in range(len(input)-1):
   cups[input[i]]=input[i+1]
cups[input[len(input)-1]]=input[0]
current=input[0]
t=0
while t<10000000:
   a=cups[current]
   b=cups[a]
   c=cups[b]
   destination=current-1
   while destination==a or destination==b or destination==c or destination<0:
      destination-=1
      if destination<0:
         destination=len(cups)-1
   cups[current]=cups[c]
   cups[c]=cups[destination]
   cups[destination]=a
   current=cups[current]
   t+=1
print((cups[0]+1)*(cups[cups[0]]+1))