
def possible_path(lst):
  h={1:[2],2:[1,"H"],3:[4],4:[3,"H"],"H":[2,4]}
  return all(y in h[x] for x,y in zip(lst,lst[1:]))

