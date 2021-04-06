
def binary_clock(time):
  time = time.replace(":","")
  r4 = "".join(str(int(i)%2) for i in time)
  r3 = "".join(str((int(i)//2)%2) for i in time)
  r2 = " " + ("".join(str((int(i)//4)%2) for i in time)[1:])
  r1 = " " + " ".join(str((int(i)//8)%2) for i in time[1::2])
  
  return [r1,r2,r3,r4]

