import copy

def step(grid):
   nextGrid=copy.deepcopy(grid)
   for row in range(HEIGHT):
      for col in range(WIDTH):
         if grid[row][col]==1 and getNeighbors(grid,row,col)==0:
            nextGrid[row][col]=2
         elif grid[row][col]==2 and getNeighbors(grid,row,col)>=5:
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
   grid=[]
   for row in range(HEIGHT):
      grid.append([])
      for col in range(WIDTH):
         if input[row][col]=='.':
            grid[row].append(0)
         else:
            grid[row].append(1)
   NEIGHBORS={}
   for row in range(HEIGHT):
      for col in range(WIDTH):
         neighborSet=set()
         testRow=row
         testCol=col
         while testRow>0:
            testRow-=1
            if grid[testRow][testCol]!=0:
               neighborSet.add((testRow,testCol))
               break
         testRow=row
         testCol=col
         while testCol<WIDTH-1:
            testCol+=1
            if grid[testRow][testCol]!=0:
               neighborSet.add((testRow,testCol))
               break
         testRow=row
         testCol=col
         while testRow<HEIGHT-1:
            testRow+=1
            if grid[testRow][testCol]!=0:
               neighborSet.add((testRow,testCol))
               break
         testRow=row
         testCol=col
         while testCol>0:
            testCol-=1
            if grid[testRow][testCol]!=0:
               neighborSet.add((testRow,testCol))
               break
         testRow=row
         testCol=col
         while testRow>0 and testCol<WIDTH-1:
            testRow-=1
            testCol+=1
            if grid[testRow][testCol]!=0:
               neighborSet.add((testRow,testCol))
               break
         testRow=row
         testCol=col
         while testRow<HEIGHT-1 and testCol<WIDTH-1:
            testRow+=1
            testCol+=1
            if grid[testRow][testCol]!=0:
               neighborSet.add((testRow,testCol))
               break
         testRow=row
         testCol=col
         while testRow<HEIGHT-1 and testCol>0:
            testRow+=1
            testCol-=1
            if grid[testRow][testCol]!=0:
               neighborSet.add((testRow,testCol))
               break
         testRow=row
         testCol=col
         while testRow>0 and testCol>0:
            testRow-=1
            testCol-=1
            if grid[testRow][testCol]!=0:
               neighborSet.add((testRow,testCol))
               break
         NEIGHBORS[(row,col)]=neighborSet
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