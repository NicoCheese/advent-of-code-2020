import copy

STEPS=100

def step(grid,neighbors):
   copyGrid=copy.deepcopy(grid)
   for row in range(len(grid)):
      for col in range(len(grid[row])-1):
         neighborCount=0
         for neighbor in neighbors[(row,col)]:
            neighborCount+=copyGrid[neighbor[0]][neighbor[1]]==1
         if copyGrid[row][col]==0 and neighborCount==2:
            grid[row][col]=1
         elif copyGrid[row][col]==1 and (neighborCount==0 or neighborCount>2):
            grid[row][col]=0
   return grid

def buildNeighbors(grid):
   neighbors={}
   for row in range(len(grid)):
      for col in range(len(grid[row])):
         neighborSet=set()
         if col>0:
            neighborSet.add((row,col-1))
         if col<len(grid[row])-1:
            neighborSet.add((row,col+1))
         if row>0:
            neighborSet.add((row-1,col))
            if row%2==0 and col>0:
               neighborSet.add((row-1,col-1))
            elif row%2==1 and col<len(grid[row])-1:
               neighborSet.add((row-1,col+1))
         if row<len(grid[row])-1:
            neighborSet.add((row+1,col))
            if row%2==0 and col>0:
               neighborSet.add((row+1,col-1))
            elif row%2==1 and col<len(grid[row])-1:
               neighborSet.add((row+1,col+1))
         neighbors[(row,col)]=neighborSet
   return neighbors

def buildGrid(tiles):
   coords=set()
   for tile in tiles:
      x=0
      y=0
      for move in tile:
         if move==1:
            x+=1
         elif move==4:
            x-=1
         elif move==0:
            if y%2==0:
               y+=1
            else:
               x+=1
               y+=1
         elif move==2:
            if y%2==0:
               y-=1
            else:
               x+=1
               y-=1
         elif move==3:
            if y%2==0:
               x-=1
               y-=1
            else:
               y-=1
         elif move==5:
            if y%2==0:
               x-=1
               y+=1
            else:
               y+=1
      coords.add((x,y))
   minX=min([coord[0] for coord in coords])
   minY=min([coord[1] for coord in coords])
   if minY%2==1:
      minY-=1
   coords=set([(coord[0]-minX,coord[1]-minY) for coord in coords])
   grid=[]
   for row in range(STEPS*2+max([coord[1] for coord in coords])+1):
      grid.append([0 for i in range(STEPS*2+max([coord[0] for coord in coords])+int(row%2==0)+1)])
   for tile in coords:
      grid[tile[1]+STEPS][tile[0]+STEPS]=1
   return grid
   
def display(grid):
   for row in grid:
      line=''
      for col in row:
         if col==0:
            line+='.'
         else:
            line+='#'
      print(line)

input=open('Input.txt','r').read().splitlines()
fliped=set()
for tile in input:
   tile=[int(i) for i in tile.replace('ne','0').replace('se','2').replace('sw','3').replace('nw','5').replace('e','1').replace('w','4')]
   last=None
   while tile!=last:
      last=tile.copy()
      while 0 in tile and 2 in tile:
         tile.remove(0)
         tile.remove(2)
         tile.append(1)
      while 1 in tile and 3 in tile:
         tile.remove(1)
         tile.remove(3)
         tile.append(2)
      while 2 in tile and 4 in tile:
         tile.remove(2)
         tile.remove(4)
         tile.append(3)
      while 3 in tile and 5 in tile:
         tile.remove(3)
         tile.remove(5)
         tile.append(4)
      while 4 in tile and 0 in tile:
         tile.remove(4)
         tile.remove(0)
         tile.append(5)
      while 5 in tile and 1 in tile:
         tile.remove(5)
         tile.remove(1)
         tile.append(0)
   while 0 in tile and 3 in tile:
      tile.remove(0)
      tile.remove(3)
   while 1 in tile and 4 in tile:
      tile.remove(1)
      tile.remove(4)
   while 2 in tile and 5 in tile:
      tile.remove(2)
      tile.remove(5)
   tile.sort()
   tile=tuple(tile)
   if tile in fliped:
      fliped.remove(tile)
   else:
      fliped.add(tile)
grid=buildGrid(fliped)
neighbors=buildNeighbors(grid)
for i in range(STEPS):
   grid=step(grid,neighbors)
count=0
for row in grid:
   for col in row:
      count+=col
print(count)