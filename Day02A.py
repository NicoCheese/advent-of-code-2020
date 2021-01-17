input=open('Input.txt','r').read().splitlines()
correct=0
for line in input:
   min=int(line[:line.index('-')])
   max=int(line[line.index('-')+1:line.index(' ')])
   target=line[line.index(' ')+1]
   if min<=line[line.index(':')+2:].count(target)<=max:
      correct+=1
print(correct)