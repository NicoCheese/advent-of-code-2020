input=open('Input.txt','r').read().splitlines()
passports=['']
for line in input:
   if not line:
      passports.append('')
   else:
      passports[-1]+=line+' '
count=0
for passport in passports:
   if passport.count(':')==8 or passport.count(':')==7 and 'cid:' not in passport:
      count+=1
print(count)