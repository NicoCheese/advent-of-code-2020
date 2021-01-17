import copy
import random

input=open('Input.txt','r').read().splitlines()
foodList=[]
for line in input:
   index=line.index('contains')
   foodList.append([line[index+9:-1].replace(',','').split(' '),line[:index-2].split(' ')])
allergens=set()
ingredients=set()
for food in foodList:
   allergens.update(food[0])
   ingredients.update(food[1])
dangerous=set()
for ingredient in ingredients:
   if ingredient not in dangerous:
      for allergen in allergens:
         isDangerous=True
         for food in foodList:
            if ingredient not in food[1] and allergen in food[0]:
               isDangerous=False
               break
         if isDangerous:
            dangerous.add(ingredient)
for food in foodList:
   remove=set()
   for ingredient in food[1]:
      if ingredient not in dangerous:
         remove.add(ingredient)
   for ingredient in remove:
      food[1].remove(ingredient)
disprovedDict={}
for ingredient in dangerous:
   if ingredient not in disprovedDict:
      disprovedDict[ingredient]=set()
   for allergen in allergens:
      disproved=True
      for food in foodList:
         if ingredient in food[1] and allergen in food[0]:
            disproved=False
         if not disproved and ingredient not in food[1] and allergen in food[0]:
            disproved=True
            break
      if disproved:
         disprovedDict[ingredient].add(allergen)
dangerousList=list(dangerous)
badCombos=[]
conclusive=False
while not conclusive:
   languageDict={}
   testDisproved=copy.deepcopy(disprovedDict)
   assignments=list(allergens)
   while assignments in badCombos:
      random.shuffle(assignments)
   badCombos.append(assignments)
   conclusive=True
   for index in range(len(dangerous)):
      if assignments[index] in disprovedDict[dangerousList[index]]:
         conclusive=False
         break
      languageDict[dangerousList[index]]=assignments[index]
   if conclusive:
      foodCopy=copy.deepcopy(foodList)
      for food in foodCopy:
         food[1]=[languageDict[ingredient] for ingredient in food[1]]
         for allergen in food[0]:
            if allergen not in food[1]:
               conclusive=False
               break
alphabetical=list(allergens)
alphabetical.sort()
for ingredient in languageDict:
   alphabetical[alphabetical.index(languageDict[ingredient])]=ingredient
alphabetical=','.join(alphabetical)
print(alphabetical)