input=open('Input.txt','r').read().splitlines()
foodList=[]
for line in input:
   index=line.index('contains')
   foodList.append((line[index+9:-1].replace(',','').split(' '),line[:index-2].split(' ')))
allergens=set()
ingredients=set()
for food in foodList:
   allergens.update(food[0])
   ingredients.update(food[1])
languageDict={}
for ingredient in ingredients:
   if ingredient not in languageDict:
      for allergen in allergens:
         isAllergen=True
         for food in foodList:
            if ingredient not in food[1] and allergen in food[0]:
               isAllergen=False
               break
         if isAllergen:
            languageDict[ingredient]=allergen
safe=ingredients-{*languageDict}
count=0
for food in foodList:
   for ingredient in food[1]:
      count+=ingredient in safe
print(count)