
def microwave_buttons(time):
  a, b = time[::-1] .split(":")
  c = [i+3 for i in range(len(b)) if b[i]!="0"]
  d = [i+1 for i in range(len(a)) if a[i]!="0"]
  e = int(a[::-1])//30 + int(b[::-1])*60 // 30
  if int(a[::-1])<30 and int(b[::-1])==0:
      return sum(c) + sum(d) + 1
  return min(e, sum(c) + sum(d)) + 1

