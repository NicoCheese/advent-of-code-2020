input=open('Input.txt','r').read().splitlines()
input=[int(i) for i in input]
input.sort()
oneCount=1
threeCount=1
for index in range(len(input)-1):
   if input[index+1]-input[index]==1:
      oneCount+=1
   elif input[index+1]-input[index]==3:
      threeCount+=1
print(oneCount*threeCount)