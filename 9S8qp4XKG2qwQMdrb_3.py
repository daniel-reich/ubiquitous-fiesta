
def ways_to_climb(h):
    if h==0 or h==1:
          return 1
    if h==2:
          return 2
    else:
          return ways_to_climb(h-1)+ways_to_climb(h-2)

