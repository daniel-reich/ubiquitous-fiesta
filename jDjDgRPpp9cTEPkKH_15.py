
def over_time(lst):
  start, end, rate, multi = lst[0],lst[1],lst[2],lst[3]
  end_fraction,start_fraction,end_rate,start_rate=0,0,0,0
  epsilon=0.0000000000001
  if (end<start):
    end+=24
  if not (int(end) == end):
    end_fraction= end-int(end)
    if (end > 17):
      end_rate=rate*multi
    else:
      end_rate=rate
    end=int(end)
  if not (int(start) == start):
    start_fraction= start-int(start)
    if (start > 17):
      start_rate=rate*multi
    else:
      start_rate=rate
    start=int(start)
  worked = round(sum([rate*multi for j in [i for i in range(start,(end))] if not j in range(9,17)]) \
    + sum([rate for j in [i for i in range(start,(end))] if j in range(9,17)]) \
    + end_fraction*end_rate -start_fraction*start_rate,3)+epsilon 
  return "$" + str("{:.2f}".format(worked))

