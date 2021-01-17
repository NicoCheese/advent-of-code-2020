input=open('Input.txt','r').read().splitlines()
testSlope=[(1,1),(3,1),(5,1),(7,1),(1,2)]
total=1
for slope in testSlope:
   x=0
   y=0
   count=0
   while y<len(input):
      if input[y][x]=='#':
         count+=1
      x=(x+slope[0])%len(input[0])
      y+=slope[1]
   total*=count
print(total)