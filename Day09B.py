input=open('Input.txt','r').read().splitlines()
input=[int(i) for i in input]
sumValues=input[:25]
for value in input[25:]:
   found=None
   for indexA in range(25):
      for indexB in range(25):
         if not found and indexA!=indexB and sumValues[indexA]+sumValues[indexB]==value:
            sumValues=sumValues[1:]+[value]
            found=value
   if not found:
      target=value
      break
for length in range(2,len(input)):
   for index in range(len(input)-length):
      test=input[index:index+length]
      if sum(test)==target:
         print(min(test)+max(test))