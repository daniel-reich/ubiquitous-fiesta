
def count_word(grid, word):
  
  rows=len(grid)
  columns=len(grid[0])
  wlen=len(word)
  count=0
  locations=[]
  final_locations=[]
​
  for x in range(rows):
    for y in range(columns):
      if grid[x][y] == word[0]:
        locations.append([x,y])
​
  for item in locations:
    up, down, left, right = True, True, True, True
    if item[1]-wlen+1<0: left=False
    if item[1]+wlen>columns: right = False
    if item[0]-wlen+1<0: up=False
    if item[0]+wlen>rows: down=False
    if up or down or left or right:
      if up:
        for z in range(wlen):
          if grid[item[0]-z][item[1]]!=word[z]:
            break
          elif z==wlen-1:
            word_location=[item, [item[0]-z, item[1]]]
            final_locations.append(word_location)
      if down:
        for z in range(wlen):
          if grid[item[0]+z][item[1]]!=word[z]:
            break
          elif z==wlen-1:
            word_location=[item, [item[0]+z, item[1]]]
            final_locations.append(word_location)
      if right:
        for z in range(wlen):
          if grid[item[0]][item[1]+z]!=word[z]:
            break
          elif z==wlen-1:
            word_location=[item, [item[0], item[1]+z]]
            final_locations.append(word_location)
      if left:
        for z in range(wlen):
          if grid[item[0]][item[1]-z]!=word[z]:
            break
          elif z==wlen-1:
            word_location=[item, [item[0], item[1]-z]]
            final_locations.append(word_location)
      if up and left:
        for z in range(wlen):
          if grid[item[0]-z][item[1]-z]!=word[z]:
            break
          elif z==wlen-1:
            word_location=[item, [item[0]-z, item[1]-z]]
            final_locations.append(word_location)
      if up and right:            
        for z in range(wlen):                
          if grid[item[0]-z][item[1]+z]!=word[z]:
            break
          elif z==wlen-1:
            word_location=[item, [item[0]-z, item[1]+z]]
            final_locations.append(word_location)
      if down and left:
        for z in range(wlen):
          if grid[item[0]+z][item[1]-z]!=word[z]:
            break
          elif z==wlen-1:
            word_location=[item, [item[0]+z, item[1]-z]]
            final_locations.append(word_location)
      if down and right:
        for z in range(wlen):
          if grid[item[0]+z][item[1]+z]!=word[z]:
            break
          elif z==wlen-1:
            word_location=[item, [item[0]+z, item[1]+z]]
            final_locations.append(word_location)
​
  for item in final_locations:
    # down and right
    if item[1][0]-item[0][0]>0 and item[1][1]-item[0][1]>0:
      for x,y in zip(range(item[1][0]-item[0][0]+1),range(item[1][1]-item[0][1]+1)):
        grid[item[0][0]+x][item[0][1]+y]=grid[item[0][0]+x][item[0][1]+y].lower()
            # print(grid[item[0][0]+x][item[0][1]+y].lower())
​
    elif item[1][0]-item[0][0]>0 and item[0][1]-item[1][1]>0:
      for x,y in zip(range(item[1][0]-item[0][0]+1),range(item[0][1]-item[1][1]+1)):
        grid[item[0][0]+x][item[0][1]-y]=grid[item[0][0]+x][item[0][1]-y].lower()
            # print(grid[item[0][0]+x][item[0][1]-y].lower())
​
    elif item[0][0]-item[1][0]>0 and item[1][1]-item[0][1]>0:
      for x,y in zip(range(item[0][0]-item[1][0]+1),range(item[1][1]-item[0][1]+1)):
        grid[item[0][0]-x][item[0][1]+y]=grid[item[0][0]-x][item[0][1]+y].lower()
            # print(grid[item[0][0]-x][item[0][1]+y].lower())
​
    elif item[0][0]-item[1][0]>0 and item[0][1]-item[1][1]>0:
        # print(item[0][0])
      for x,y in zip(range(item[0][0]-item[1][0]+1),range(item[0][1]-item[1][1]+1)):
        grid[item[0][0]-x][item[0][1]-y]=grid[item[0][0]-x][item[0][1]-y].lower()
            # print(grid[item[0][0]-x][item[0][1]-y].lower())
            
    elif item[1][0]-item[0][0]>0:
      for x in range((item[1][0]-item[0][0])+1):
        grid[item[0][0]+x][item[0][1]]=grid[item[0][0]+x][item[0][1]].lower()
    elif item[0][0]-item[1][0]>0:
      for x in range((item[0][0]-item[1][0])+1):
            # print('hi')
        grid[item[0][0]-x][item[0][1]]=grid[item[0][0]-x][item[0][1]].lower()
    elif item[1][1]-item[0][1]>0:
      for y in range(item[1][1]-item[0][1]+1):
            # print('hi')
        grid[item[0][0]][item[0][1]+y]=grid[item[0][0]][item[0][1]+y].lower()
            # print(grid[item[0][0]][item[0][1]+y])
    elif item[0][1]-item[1][1]>0:
      for y in range(item[0][1]-item[1][1]+1):
            # print('hi')
        grid[item[0][0]][item[0][1]-y]=grid[item[0][0]][item[0][1]-y].lower()
            # print(grid[item[0][0]][item[0][1]+y])
​
  answer=(len(final_locations),grid)
  return(answer)

