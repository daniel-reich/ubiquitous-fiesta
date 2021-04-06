
def time_sum(times):
​
  times = [times[i].split(':') for i in range(len(times))]
  new = []
  
  for i in range(3):
    new.append(sum(map(int,[time[i] for time in times])))
  
  return [(new[0] + (new[1] // 60)), (new[1] + (new[2] // 60)) % 60, new[2] % 60]

