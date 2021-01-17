def evaluate(expression):
   terms=[]
   operators=[]
   depth=0
   capture=''
   for char in expression:
      if depth>0:
         capture+=char
      if char=='(':
         depth+=1
      elif char==')':
         depth-=1
         if depth==0:
            terms.append(evaluate(capture[:-1]))
            capture=''
      elif depth==0:
         if char=='*' or char=='+':
            operators.append(char)
         else:
            terms.append(int(char))
   while len(terms)>1:
      if '+' in operators:
         index=operators.index('+')
      else:
         index=operators.index('*')
      term=terms.pop(index)
      operator=operators.pop(index)
      if operator=='*':
         terms[index]=term*terms[index]
      else:
         terms[index]=term+terms[index]
   return terms[0]

input=open('Input.txt','r').read().splitlines()
total=0
for line in input:
   total+=evaluate(line.replace(' ',''))
print(total)