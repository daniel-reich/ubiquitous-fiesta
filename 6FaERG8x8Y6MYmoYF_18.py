
def dice_score(throw):
   d = {1:(1000,100),
        2:(200,0),
        3:(300,0),
        4:(400,0),
        5:(500,50),
        6:(600,0)}
   tot = 0
   for t in range(1,7):
      if t in throw:
         v3, v1 = d[t]
         cnt = throw.count(t)
         if cnt >= 3:
            tot += v3
            cnt -= 3
         tot += cnt * v1
   return tot

