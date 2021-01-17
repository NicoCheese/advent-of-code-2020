import copy

def buildTileGrid(tileNeighbors):
   corners=set()
   edges=set()
   middles=set()
   for tile in tileNeighbors:
      if len(tileNeighbors[tile])==2:
         corners.add(tile)
      elif len(tileNeighbors[tile])==3:
         edges.add(tile)
      else:
         middles.add(tile)
   tileGrid=[[0 for i in range(GRIDWIDTH)] for e in range(GRIDWIDTH)]
   tileGrid[0][0]=corners.pop()
   for x in range(1,GRIDWIDTH-1):
      for tile in edges:
         if tileGrid[x-1][0] in tileNeighbors[tile]:
            tileGrid[x][0]=tile
            edges.discard(tile)
            break
   for y in range(1,GRIDWIDTH-1):
      for tile in edges:
         if tileGrid[0][y-1] in tileNeighbors[tile]:
            tileGrid[0][y]=tile
            edges.discard(tile)
            break
   for tile in corners:
      if tileGrid[0][-2] in tileNeighbors[tile]:
         tileGrid[0][-1]=tile
         corners.discard(tile)
         break
   for tile in corners:
      if tileGrid[-2][0] in tileNeighbors[tile]:
         tileGrid[-1][0]=tile
         corners.discard(tile)
         break
   for x in range(1,GRIDWIDTH-1):
      for tile in edges:
         if tileGrid[x-1][-1] in tileNeighbors[tile]:
            tileGrid[x][-1]=tile
            edges.discard(tile)
            break
   for y in range(1,GRIDWIDTH-1):
      for tile in edges:
         if tileGrid[-1][y-1] in tileNeighbors[tile]:
            tileGrid[-1][y]=tile
            edges.discard(tile)
            break
   tileGrid[-1][-1]=corners.pop()
   for x in range(1,GRIDWIDTH-1):
      for y in range(1,GRIDWIDTH-1):
         for tile in middles:
            if tileGrid[x-1][y] in tileNeighbors[tile] and tileGrid[x][y-1] in tileNeighbors[tile]:
               tileGrid[x][y]=tile
               middles.discard(tile)
               break
   return tileGrid

def getGroup(tile):
   group=[]
   group.append(tile)
   group.append(flip(group[-1]))
   group.append(rotate(group[-2]))
   group.append(flip(group[-1]))
   group.append(rotate(group[-2]))
   group.append(flip(group[-1]))
   group.append(rotate(group[-2]))
   group.append(flip(group[-1]))
   return group
      
def rotate(tile):
   width=len(tile)
   rotated=copy.deepcopy(tile)
   for level in range(width//2):
      for pos in range(level,width-level):
         rotated[pos][level]=tile[level][-pos-1]
         rotated[level][-pos-1]=tile[-pos-1][-level-1]
         rotated[-pos-1][-level-1]=tile[-level-1][pos]
         rotated[-level-1][pos]=tile[pos][level]
   return rotated

def flip(tile):
   flipped=[]
   for row in tile:
      flipped.append(row[::-1])
   return flipped

def getEdges(tile):
   edges=[]
   edges.append(tile[0])
   edges.append(tile[-1])
   edges.append([tile[row][0] for row in range(TILEWIDTH)])
   edges.append([tile[row][-1] for row in range(TILEWIDTH)])
   return edges

def setup(input):
   global TILEWIDTH
   global GRIDWIDTH
   tiles={}
   for line in input:
      if ':' in line:
         tiles[line[-5:-1]]=[]
         current=line[-5:-1]
      elif line:
         tiles[current].append([int(char=='#') for char in line])
         TILEWIDTH=len(line)
   GRIDWIDTH=int(len(tiles)**.5)
   return tiles

def displayFancy(tile):
   for row in range(len(tile)):
      if row!=0 and row%10==0:
         print('-'*(TILEWIDTH*GRIDWIDTH+GRIDWIDTH-1))
      nextPrint=''
      for type in tile[row]:
         if len(nextPrint)!=0 and (len(nextPrint)-nextPrint.count('|'))%10==0:
            nextPrint+='|'
         if type==0:
            nextPrint+='.'
         else:
            nextPrint+='#'
      print(nextPrint)
      
def display(tile):
   for row in range(len(tile)):
      nextPrint=''
      for type in tile[row]:
         if type==0:
            nextPrint+='.'
         else:
            nextPrint+='#'
      print(nextPrint)

input=open('Input.txt','r').read().splitlines()
tiles=setup(input)
for tile in tiles:
   tiles[tile]=getGroup(tiles[tile])
tileNeighbors={}
for tileA in tiles:
   tileNeighbors[tileA]=set()
   for tileB in tiles:
      if tileA!=tileB:
         for groupA in tiles[tileA]:
            for groupB in tiles[tileB]:
               for edge in getEdges(groupA):
                  if edge in getEdges(groupB):
                     tileNeighbors[tileA].add(tileB)
tileGrid=buildTileGrid(tileNeighbors)
for start in range(8):
   queue=tileNeighbors[tileGrid[1][1]].copy()
   visited={tileGrid[1][1]}
   grid=[[0 for col in range(GRIDWIDTH)] for row in range(GRIDWIDTH)]
   grid[1][1]=tiles[tileGrid[1][1]][start]
   while queue:
      current=queue.pop()
      if current not in visited:
         visited.add(current)
         queue=queue|tileNeighbors[current]
         for row in range(GRIDWIDTH):
            for col in range(GRIDWIDTH):
               if tileGrid[row][col]==current:
                  location=(row,col)
                  break
         if location[0]>0 and grid[location[0]-1][location[1]]!=0:
            parent=getEdges(grid[location[0]-1][location[1]])[1]
            edge=0
         elif location[0]<GRIDWIDTH-1 and grid[location[0]+1][location[1]]!=0:
            parent=getEdges(grid[location[0]+1][location[1]])[0]
            edge=1
         elif location[1]>0 and grid[location[0]][location[1]-1]!=0:
            parent=getEdges(grid[location[0]][location[1]-1])[3]
            edge=2
         elif location[1]<GRIDWIDTH-1 and grid[location[0]][location[1]+1]!=0:
            parent=getEdges(grid[location[0]][location[1]+1])[2]
            edge=3
         for group in tiles[current]:
            if parent==getEdges(group)[edge]:
               grid[location[0]][location[1]]=group
               break
   complete=True
   for row in grid:
      if 0 in row:
         complete=False
   if complete:
      break
combined=[]
count=0
for row in range(GRIDWIDTH):
   for tileRow in range(1,TILEWIDTH-1):
      combinedRow=[]
      for col in range(GRIDWIDTH):
         combinedRow+=grid[row][col][tileRow][1:-1]
      count+=combinedRow.count(1)
      combined.append(combinedRow)
seaMonster='                  # \n#    ##    ##    ###\n #  #  #  #  #  #   '
monsterSize=seaMonster.count('#')
seaMonster=[[int(char=='#') for char in line] for line in seaMonster.split('\n')]
for image in getGroup(combined):
   seaMonsters=0
   for row in range((TILEWIDTH-2)*GRIDWIDTH-len(seaMonster)):
      for col in range((TILEWIDTH-2)*GRIDWIDTH-len(seaMonster[0])):
         testMonster=[image[row+height][col:col+len(seaMonster[0])] for height in range(len(seaMonster))]
         isMonster=True
         for level in range(len(seaMonster)):
            for index in range(len(seaMonster[level])):
               if seaMonster[level][index]==1 and testMonster[level][index]==0:
                  isMonster=False
                  break
         seaMonsters+=isMonster
   if seaMonsters:
      print(count-seaMonsters*monsterSize)
      break