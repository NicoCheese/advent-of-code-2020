input=open('Input.txt','r').read().splitlines()
bagDict={}
for rule in input:
   if ' no ' not in rule:
      bagIndex=rule.index(' bag')
      for count in range(rule.count(' bag')-1):
         bagIndex=rule.index(' bag',bagIndex+1)
         bag=rule[rule.rindex(' ',0,rule.rindex(' ',0,bagIndex))+1:bagIndex]
         if bag not in bagDict:
            bagDict[bag]=set()
         bagDict[bag].add(rule[:rule.index(' bag')])
canContain=bagDict['shiny gold']
complete=False
while(not complete):
   completeCheck=canContain.copy()
   for contains in canContain:
      if contains in bagDict:
         canContain=canContain|bagDict[contains]
   if completeCheck==canContain:
      complete=True
print(len(canContain))