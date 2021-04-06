
def time_sum(times):
  from functools import reduce
  times_list = [list(map(int,one_time.split(':'))) for one_time in times]
  return reduce(lambda t1,t2:
    [(t1[0]+t2[0]+(t1[1]+t2[1])//60),\
    (t1[1]+t2[1]+(t1[2]+t2[2])//60) % 60,\
    (t1[2]+t2[2]) % 60],times_list) if times_list else [0,0,0]

