
def mineral_formation(cave):
 stalac = False
 stalag = False
 for x in cave[0]:
    if x != 0:
           stalac = True
 for x in cave[3]:
  if x != 0:
          stalag = True
 if (stalag and stalac) == True:
   return "both"
 elif stalag == True:
   return "stalagmites"
 elif stalac == True:
   return "stalactites"

