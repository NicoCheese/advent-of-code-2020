import re

def countNestedBags(bag,bagDict):
   if bag in bagDict:
      count=0
      for innerBag in bagDict[bag]:
         count+=(countNestedBags(innerBag[0],bagDict)+1)*innerBag[1]
      return count
   return 0

input=open('Input.txt','r').read().splitlines()
bagDict={}
for rule in input:
   if ' no ' not in rule:
      contains=[]
      bagIndex=rule.index(' bag')
      for count in range(rule.count(' bag')-1):
         bagIndex=rule.index(' bag',bagIndex+1)
         contains.append(rule[rule.rindex(' ',0,rule.rindex(' ',0,bagIndex))+1:bagIndex])
      bagDict[rule[:rule.index(' bag')]]=set(zip(contains,[int(digit) for digit in re.findall('\d',rule)]))
print(countNestedBags('shiny gold',bagDict))