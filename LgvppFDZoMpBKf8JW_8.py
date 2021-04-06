
def digital_clock(seconds):
  a = seconds//3600
  b = (seconds - a*3600)//60
  c = seconds - a*3600 - b*60
  d = [str(a%24), str(b), str(c)]
  return ":".join("0"+i if len(i)==1 else i for i in d)

