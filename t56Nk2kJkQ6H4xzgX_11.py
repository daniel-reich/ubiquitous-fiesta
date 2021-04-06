
def swap_xy(txt):
  txt = txt.replace("(","")
  txt = txt.replace(")","")
  txt = txt.replace(" ","")
  arr = list(map(int,txt.split(',')))
  brr = []
  for i in range(0,len(arr),2):
    brr.append("(" + str(arr[i+1]) + ", " + str(arr[i]) + ")")
  return ", ".join(brr)

