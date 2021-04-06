
def get_path_length(world, width, height):
  world=world.replace('m','m0').split(',')
  for c in range(width*height):
    for idx,i in enumerate(world):
      if i=='m{}'.format(c):
        h,w=idx//height,idx-idx//height*height
        for d in [(1,1),(1,-1),(1,0),(0,1),(0,-1),(-1,1),(-1,0),(-1,-1)]:
          hx,wx=h+d[0],w+d[1]
          if width>wx>=0 and height>hx>=0:
            idxx=wx+hx*height
            if world[idxx]=='.':world[idxx]='m{}'.format(c+1)
            if world[idxx]=='h':return c+1
  return -1

