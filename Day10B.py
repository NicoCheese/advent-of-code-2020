input=open('Input.txt','r').read().splitlines()
adapters=[int(i) for i in input]
adapters.append(0)
adapters.append(max(adapters)+3)
adapters.sort()
adapterGroups=[]
lastIndex=0
for index in range(len(adapters)-1):
   if adapters[index+1]-adapters[index]==3:
      if len(adapters[lastIndex:index+1])>2:
         adapterGroups.append(adapters[lastIndex:index+1])
         lastIndex=index+1
permutations=1
for adapterGroup in adapterGroups:
   openSet=[tuple(adapterGroup)]
   closedSet=set()
   while openSet:
      adapterGroup=openSet.pop()
      closedSet.add(tuple(adapterGroup))
      for index in range(len(adapterGroup)):
         if index<len(adapterGroup)-2 and adapterGroup[index+2]-adapterGroup[index]<=3:
            next=tuple(adapterGroup[:index+1]+adapterGroup[index+2:])
            if next not in closedSet:
               openSet.append(next)
         elif index<len(adapterGroup)-3 and adapterGroup[index+3]-adapterGroup[index]<=3:
            next=tuple(adapterGroup[:index+1]+adapterGroup[index+3:])
            if next not in closedSet:
               openSet.append(next)
   permutations*=len(closedSet)
print(permutations)