
def colour_harmony(anchor, c):
  colours=["red","red-orange","orange","yellow-orange","yellow","yellow-green"]
  colours+=["green","blue-green","blue","blue-violet","violet","red-violet"]
  
  combs = {}
  combs["complementary"] = [0,6]
  combs["analogous"] = [0,1,-1]
  combs["split_complementary"] = [0,5,-5]
  combs["triadic"] = [0,4,-4]
  combs["rectangle"] = [0,2,6,-4]
  combs["square"] = [0,3,6,-3]
  
  r = colours.index(anchor)
  return {colours[(r+i)%12] for i in combs[c]}

