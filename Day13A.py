input=open('Input.txt','r').read().splitlines()
arrival=int(input[0])
buses=[int(id) for id in input[1].split(',') if id!='x']
waits=[id-arrival%id for id in buses]
print(min(waits)*buses[waits.index(min(waits))])