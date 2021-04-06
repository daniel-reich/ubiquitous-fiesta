
import math
​
def over_time(lst):
  over = lst[1] - 17
  if lst[0] >= 17:
    main = (lst[1]-lst[0]) * lst[2] * lst[3]
  else:
    if over > 0:
      main = ((17 - lst[0]) * lst[2]) + (over * lst[2] * lst[3])
    else:
      main = (lst[1] - lst[0]) * lst[2]
  print(main)
  if main - math.floor(main) < 0.5:
    main = "$" + str('{:.2f}'.format(math.floor(main * 100) / 100))
  else:
    main = "$" + str('{:.2f}'.format(math.ceil(main * 100) / 100))
  return (main)

