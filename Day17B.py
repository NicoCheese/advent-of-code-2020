import copy

STEPS=6

def step(grid):
   copyGrid=copy.deepcopy(grid)
   for w in range(wLength):
      for x in range(xLength):
         for y in range(yLength):
            for z in range(zLength):
               neighborCount=getNeighbors((w,x,y,z),copyGrid)
               if copyGrid[w][x][y][z]==0 and neighborCount==3:
                  grid[w][x][y][z]=1
               elif copyGrid[w][x][y][z]==1 and (neighborCount<2 or neighborCount>3):
                  grid[w][x][y][z]=0
   return grid

def getNeighbors(coords,grid):
   count=0
   for neighbor in neighbors[coords]:
      count+=grid[neighbor[0]][neighbor[1]][neighbor[2]][neighbor[3]]
   return count

def setup(input):
   global wLength
   global xLength
   global yLength
   global zLength
   global neighbors
   wLength=STEPS*2+1
   xLength=len(input[0])+STEPS*2
   yLength=len(input)+STEPS*2
   zLength=STEPS*2+1
   grid=[]
   for w in range(wLength):
      grid.append([])
      for x in range(xLength):
         grid[w].append([])
         for y in range(yLength):
            grid[w][x].append([])
            grid[w][x][y]=[0 for z in range(zLength)]
   for x in range(xLength-STEPS*2):
      for y in range(yLength-STEPS*2):
         if input[y][x]=='#':
            grid[wLength//2][x+STEPS][y+STEPS][zLength//2]=1
   neighbors={}
   for w in range(wLength):
      for x in range(xLength):
         for y in range(yLength):
            for z in range(zLength):
               neighborList=[]
               if w>0:
                  neighborList.append((w-1,x,y,z))
                  if x>0:
                     neighborList.append((w-1,x-1,y,z))
                     if y>0:
                        neighborList.append((w-1,x-1,y-1,z))
                        if z>0:
                           neighborList.append((w-1,x-1,y-1,z-1))
                        if z<zLength-1:
                           neighborList.append((w-1,x-1,y-1,z+1))
                     if y<yLength-1:
                        neighborList.append((w-1,x-1,y+1,z))
                        if z>0:
                           neighborList.append((w-1,x-1,y+1,z-1))
                        if z<zLength-1:
                           neighborList.append((w-1,x-1,y+1,z+1))
                     if z>0:
                        neighborList.append((w-1,x-1,y,z-1))
                     if z<zLength-1:
                        neighborList.append((w-1,x-1,y,z+1))
                  if x<xLength-1:
                     neighborList.append((w-1,x+1,y,z))
                     if y>0:
                        neighborList.append((w-1,x+1,y-1,z))
                        if z>0:
                           neighborList.append((w-1,x+1,y-1,z-1))
                        if z<zLength-1:
                           neighborList.append((w-1,x+1,y-1,z+1))
                     if y<yLength-1:
                        neighborList.append((w-1,x+1,y+1,z))
                        if z>0:
                           neighborList.append((w-1,x+1,y+1,z-1))
                        if z<zLength-1:
                           neighborList.append((w-1,x+1,y+1,z+1))
                     if z>0:
                        neighborList.append((w-1,x+1,y,z-1))
                     if z<zLength-1:
                        neighborList.append((w-1,x+1,y,z+1))
                  if y>0:
                     neighborList.append((w-1,x,y-1,z))
                     if z>0:
                        neighborList.append((w-1,x,y-1,z-1))
                     if z<zLength-1:
                        neighborList.append((w-1,x,y-1,z+1))
                  if y<yLength-1:
                     neighborList.append((w-1,x,y+1,z))
                     if z>0:
                        neighborList.append((w-1,x,y+1,z-1))
                     if z<zLength-1:
                        neighborList.append((w-1,x,y+1,z+1))
                  if z>0:
                     neighborList.append((w-1,x,y,z-1))
                  if z<zLength-1:
                     neighborList.append((w-1,x,y,z+1))
               if w<wLength-1:
                  neighborList.append((w+1,x,y,z))
                  if x>0:
                     neighborList.append((w+1,x-1,y,z))
                     if y>0:
                        neighborList.append((w+1,x-1,y-1,z))
                        if z>0:
                           neighborList.append((w+1,x-1,y-1,z-1))
                        if z<zLength-1:
                           neighborList.append((w+1,x-1,y-1,z+1))
                     if y<yLength-1:
                        neighborList.append((w+1,x-1,y+1,z))
                        if z>0:
                           neighborList.append((w+1,x-1,y+1,z-1))
                        if z<zLength-1:
                           neighborList.append((w+1,x-1,y+1,z+1))
                     if z>0:
                        neighborList.append((w+1,x-1,y,z-1))
                     if z<zLength-1:
                        neighborList.append((w+1,x-1,y,z+1))
                  if x<xLength-1:
                     neighborList.append((w+1,x+1,y,z))
                     if y>0:
                        neighborList.append((w+1,x+1,y-1,z))
                        if z>0:
                           neighborList.append((w+1,x+1,y-1,z-1))
                        if z<zLength-1:
                           neighborList.append((w+1,x+1,y-1,z+1))
                     if y<yLength-1:
                        neighborList.append((w+1,x+1,y+1,z))
                        if z>0:
                           neighborList.append((w+1,x+1,y+1,z-1))
                        if z<zLength-1:
                           neighborList.append((w+1,x+1,y+1,z+1))
                     if z>0:
                        neighborList.append((w+1,x+1,y,z-1))
                     if z<zLength-1:
                        neighborList.append((w+1,x+1,y,z+1))
                  if y>0:
                     neighborList.append((w+1,x,y-1,z))
                     if z>0:
                        neighborList.append((w+1,x,y-1,z-1))
                     if z<zLength-1:
                        neighborList.append((w+1,x,y-1,z+1))
                  if y<yLength-1:
                     neighborList.append((w+1,x,y+1,z))
                     if z>0:
                        neighborList.append((w+1,x,y+1,z-1))
                     if z<zLength-1:
                        neighborList.append((w+1,x,y+1,z+1))
                  if z>0:
                     neighborList.append((w+1,x,y,z-1))
                  if z<zLength-1:
                     neighborList.append((w+1,x,y,z+1))
               if x>0:
                  neighborList.append((w,x-1,y,z))
                  if y>0:
                     neighborList.append((w,x-1,y-1,z))
                     if z>0:
                        neighborList.append((w,x-1,y-1,z-1))
                     if z<zLength-1:
                        neighborList.append((w,x-1,y-1,z+1))
                  if y<yLength-1:
                     neighborList.append((w,x-1,y+1,z))
                     if z>0:
                        neighborList.append((w,x-1,y+1,z-1))
                     if z<zLength-1:
                        neighborList.append((w,x-1,y+1,z+1))
                  if z>0:
                     neighborList.append((w,x-1,y,z-1))
                  if z<zLength-1:
                     neighborList.append((w,x-1,y,z+1))
               if x<xLength-1:
                  neighborList.append((w,x+1,y,z))
                  if y>0:
                     neighborList.append((w,x+1,y-1,z))
                     if z>0:
                        neighborList.append((w,x+1,y-1,z-1))
                     if z<zLength-1:
                        neighborList.append((w,x+1,y-1,z+1))
                  if y<yLength-1:
                     neighborList.append((w,x+1,y+1,z))
                     if z>0:
                        neighborList.append((w,x+1,y+1,z-1))
                     if z<zLength-1:
                        neighborList.append((w,x+1,y+1,z+1))
                  if z>0:
                     neighborList.append((w,x+1,y,z-1))
                  if z<zLength-1:
                     neighborList.append((w,x+1,y,z+1))
               if y>0:
                  neighborList.append((w,x,y-1,z))
                  if z>0:
                     neighborList.append((w,x,y-1,z-1))
                  if z<zLength-1:
                     neighborList.append((w,x,y-1,z+1))
               if y<yLength-1:
                  neighborList.append((w,x,y+1,z))
                  if z>0:
                     neighborList.append((w,x,y+1,z-1))
                  if z<zLength-1:
                     neighborList.append((w,x,y+1,z+1))
               if z>0:
                  neighborList.append((w,x,y,z-1))
               if z<zLength-1:
                  neighborList.append((w,x,y,z+1))
               neighbors[(w,x,y,z)]=neighborList
   return grid

input=open('Input.txt','r').read().splitlines()
grid=setup(input)
for i in range(STEPS):
   grid=step(grid)
count=0
for w in range(wLength):
   for x in range(xLength):
      for y in range(yLength):
         for z in range(zLength):
            count+=grid[w][x][y][z]
print(count)