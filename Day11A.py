import copy

def step(grid):
   nextGrid=copy.deepcopy(grid)
   for row in range(HEIGHT):
      for col in range(WIDTH):
         if grid[row][col]==1 and getNeighbors(grid,row,col)==0:
            nextGrid[row][col]=2
         elif grid[row][col]==2 and getNeighbors(grid,row,col)>=4:
            nextGrid[row][col]=1
   return nextGrid

def getNeighbors(grid,row,col):
   adjacent=0
   for neighbor in NEIGHBORS[(row,col)]:
      if grid[neighbor[0]][neighbor[1]]==2:
         adjacent+=1
   return adjacent

def setup(input):
   global WIDTH
   global HEIGHT
   global NEIGHBORS
   WIDTH=len(input[0])
   HEIGHT=len(input)
   NEIGHBORS={}
   for row in range(HEIGHT):
      for col in range(WIDTH):
         neighborSet=set()
         if row>0:
            neighborSet.add((row-1,col))
            if col>0:
               neighborSet.add((row-1,col-1))
            if col<WIDTH-1:
               neighborSet.add((row-1,col+1))
         if row<HEIGHT-1:
            neighborSet.add((row+1,col))
            if col>0:
               neighborSet.add((row+1,col-1))
            if col<WIDTH-1:
               neighborSet.add((row+1,col+1))
         if col>0:
            neighborSet.add((row,col-1))
         if col<WIDTH-1:
            neighborSet.add((row,col+1))
         NEIGHBORS[(row,col)]=neighborSet
   grid=[]
   for row in range(HEIGHT):
      grid.append([])
      for col in range(WIDTH):
         if input[row][col]=='.':
            grid[row].append(0)
         else:
            grid[row].append(1)
   return grid

def display(grid):
   for line in grid:
      nextPrint=''
      for type in line:
         if type==0:
            nextPrint+='.'
         elif type==1:
            nextPrint+='L'
         else:
            nextPrint+='#'
      print(nextPrint)

input=open('Input.txt','r').read().splitlines()
grid=setup(input)
isStable=False
while not isStable:
   oldGrid=grid
   grid=step(grid)
   if grid==oldGrid:
      isStable=True
count=0
for col in range(WIDTH):
   for row in range(HEIGHT):
      count+=grid[row][col]==2
print(count)