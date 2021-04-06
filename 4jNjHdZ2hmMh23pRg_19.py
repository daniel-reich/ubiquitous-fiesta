
def cutting_grass(lst, *cuts):
  shaves = []
  
  for cut in cuts:
    new_heights = [height - cut for height in lst]
​
    if any(height < 1 for height in new_heights):
      shaves.append('Done')
    else:
      shaves.append(new_heights)
​
    lst = new_heights
​
  return shaves

