input=open('Input.txt','r').read().splitlines()
for testIndex in range(len(input)):
   testInput=input.copy()
   if input[testIndex][:3]=='jmp':
      testInput[testIndex]='nop'+input[testIndex][3:]
   elif input[testIndex][:3]=='nop':
      testInput[testIndex]='jmp'+input[testIndex][3:]
   visited=set()
   accumulator=0
   index=0
   while index<len(testInput) and index not in visited:
      visited.add(index)
      op=testInput[index][:3]
      arg=int(testInput[index][4:])
      if op=='acc':
         accumulator+=arg
         index+=1
      elif op=='jmp':
         index+=arg
      else:
         index+=1
   if index>=len(testInput):
      break
print(accumulator)