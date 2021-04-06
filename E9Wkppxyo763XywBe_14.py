
def binary_clock(time):
  time = [bin(int(i))[2:] for i in time if i.isdigit()]
  for i,v in enumerate(time): time[i] = "{:>4}".format("0"*(int("243434"[i])-len(v))+v)
  return [''.join(i[j] for i in time) for j in range(4)]

