def encrypt(value,subject,loop):
   for i in range(loop):
      value*=subject
      value%=20201227
   return value

input=open('Input.txt','r').read().splitlines()
door=int(input[0])
key=int(input[1])
loop=0
value=1
found=False
while not found:
   loop+=1
   value=encrypt(value,7,1)
   found=value==door
print(encrypt(1,key,loop))