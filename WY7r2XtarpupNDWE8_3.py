
def tower_of_hanoi(disks, move):
  t1 = []
  t2 = [disks + 1]
  t3 = [disks + 1]
  b = 1
  for a in range(1, disks + 1):
    t1.insert(0,a)
  for a in range(move):
    if disks % 2 == 1:  
      if b == 1:
        t3.append(t1.pop()) if t1[-1] < t3[-1] else t1.append(t3.pop())
        b = 2
      elif b == 2:
        t2.append(t1.pop()) if t1[-1] < t2[-1] else t1.append(t2.pop())
        b = 3
      elif b == 3:
        t2.append(t3.pop()) if t3[-1] < t2[-1] else t3.append(t2.pop())
        b = 1
    else:
      if b == 1:
        t2.append(t1.pop()) if t1[-1] < t2[-1] else t1.append(t2.pop())
        b = 2
      elif b == 2:
        t3.append(t1.pop()) if t1[-1] < t3[-1] else t1.append(t3.pop())
        b = 3
      elif b == 3:
        t2.append(t3.pop()) if t3[-1] < t2[-1] else t3.append(t2.pop())
        b = 1
  t2.pop(0)
  t3.pop(0)
  return (t1,t2,t3)

