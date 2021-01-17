import copy

STEPS=6

def step(grid):
   copyGrid=copy.deepcopy(grid)
   for x in range(xLength):
      for y in range(yLength):
         for z in range(zLength):
            neighborCount=getNeighbors((x,y,z),copyGrid)
            if copyGrid[x][y][z]==0 and neighborCount==3:
               grid[x][y][z]=1
            elif copyGrid[x][y][z]==1 and (neighborCount<2 or neighborCount>3):
               grid[x][y][z]=0
   return grid

def getNeighbors(coords,grid):
   count=0
   for neighbor in neighbors[coords]:
      count+=grid[neighbor[0]][neighbor[1]][neighbor[2]]
   return count

def setup(input):
   global xLength
   global yLength
   global zLength
   global neighbors
   xLength=len(input[0])+STEPS*2
   yLength=len(input)+STEPS*2
   zLength=STEPS*2+1
   grid=[]
   for x in range(xLength):
      grid.append([])
      for y in range(yLength):
         grid[x].append([])
         grid[x][y]=[0 for z in range(zLength)]
   for x in range(xLength-STEPS*2):
      for y in range(yLength-STEPS*2):
         if input[y][x]=='#':
            grid[x+STEPS][y+STEPS][zLength//2]=1
   neighbors={}
   for x in range(xLength):
      for y in range(yLength):
         for z in range(zLength):
            neighborList=[]
            if x>0:
               neighborList.append((x-1,y,z))
               if y>0:
                  neighborList.append((x-1,y-1,z))
                  if z>0:
                     neighborList.append((x-1,y-1,z-1))
                  if z<zLength-1:
                     neighborList.append((x-1,y-1,z+1))
               if y<yLength-1:
                  neighborList.append((x-1,y+1,z))
                  if z>0:
                     neighborList.append((x-1,y+1,z-1))
                  if z<zLength-1:
                     neighborList.append((x-1,y+1,z+1))
               if z>0:
                  neighborList.append((x-1,y,z-1))
               if z<zLength-1:
                  neighborList.append((x-1,y,z+1))
            if x<xLength-1:
               neighborList.append((x+1,y,z))
               if y>0:
                  neighborList.append((x+1,y-1,z))
                  if z>0:
                     neighborList.append((x+1,y-1,z-1))
                  if z<zLength-1:
                     neighborList.append((x+1,y-1,z+1))
               if y<yLength-1:
                  neighborList.append((x+1,y+1,z))
                  if z>0:
                     neighborList.append((x+1,y+1,z-1))
                  if z<zLength-1:
                     neighborList.append((x+1,y+1,z+1))
               if z>0:
                  neighborList.append((x+1,y,z-1))
               if z<zLength-1:
                  neighborList.append((x+1,y,z+1))
            if y>0:
               neighborList.append((x,y-1,z))
               if z>0:
                  neighborList.append((x,y-1,z-1))
               if z<zLength-1:
                  neighborList.append((x,y-1,z+1))
            if y<yLength-1:
               neighborList.append((x,y+1,z))
               if z>0:
                  neighborList.append((x,y+1,z-1))
               if z<zLength-1:
                  neighborList.append((x,y+1,z+1))
            if z>0:
               neighborList.append((x,y,z-1))
            if z<zLength-1:
               neighborList.append((x,y,z+1))
            neighbors[(x,y,z)]=neighborList
   return grid

input=open('Input.txt','r').read().splitlines()
grid=setup(input)
for i in range(STEPS):
   grid=step(grid)
count=0
for x in range(xLength):
   for y in range(yLength):
      for z in range(zLength):
         count+=grid[x][y][z]
print(count)