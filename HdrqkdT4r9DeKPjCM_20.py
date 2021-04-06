
def is_polygonal(n):
      if n == 1:
          return "0th of all"
      result = []
      for gonal_num in range(3, (n-1)*2+1):
           if ((n-1)*2) % gonal_num != 0:
                continue
           else:
                for level_num in range(1, ((n-1)*2)//gonal_num + 1):
                     if level_num * (level_num +1) * gonal_num == (n-1) * 2:
                         if str(level_num) == "11":
                             result.append(str(level_num) + "th" + " " + str(gonal_num) + "-gonal number")
                         elif str(level_num) == "12":
                             result.append(str(level_num) + "th" + " " + str(gonal_num) + "-gonal number")
                         elif str(level_num) == "13":
                             result.append(str(level_num) + "th" + " " + str(gonal_num) + "-gonal number")
                             
                         elif str(level_num)[-1] == '1':
                             result.append(str(level_num) + "st" + " " + str(gonal_num) + "-gonal number")
                         elif str(level_num)[-1] == '2':
                                 result.append(str(level_num) + "nd" + " " + str(gonal_num) + "-gonal number")
                         elif str(level_num)[-1] == '3':
                             result.append(str(level_num) + "rd" + " " + str(gonal_num) + "-gonal number")
                         else:
                             result.append(str(level_num) + "th" + " " + str(gonal_num) + "-gonal number")
      if result == []:
           return False
      return result

