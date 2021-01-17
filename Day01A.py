input=open('Input.txt','r').read().splitlines()
for i in input:
   for e in input:
         if int(i)+int(e)==2020:
            print(int(i)*int(e))