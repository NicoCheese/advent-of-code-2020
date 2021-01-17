import copy
import re

def condense(number,rules):
   ruleCopy=copy.deepcopy(rules)
   if 'a' in ruleCopy[number]:
      return 'a'
   if 'b' in ruleCopy[number]:
      return 'b'
   for rule in re.findall('\d+',ruleCopy[number]):
      ruleCopy[number]=(' '+ruleCopy[number]+' ').replace(' '+rule+' ',' '+condense(rule,ruleCopy)+' ')
   return '('+ruleCopy[number].replace(' ','')+')'

input=open('Input.txt','r').read().splitlines()
rules={}
for line in input:
   if not line:
      break
   index=line.index(':')
   rules[line[:index]]=line[index+2:]
rule='^'+condense('0',rules)+'$'
count=0
for line in input[::-1]:
   if not line:
      break
   if re.findall(rule,line):
      count+=1
print(count)