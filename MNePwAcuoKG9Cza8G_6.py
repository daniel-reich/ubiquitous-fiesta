
def build_staircase(height, block):
  def build_list(height, block, l):
    return ([block for i in range(height)] + 
            ["_" for i in range(height,l)]  )
  ret = []
  for i in range(1,height + 1):
    ret.append(build_list(i, block, height))
  return ret

