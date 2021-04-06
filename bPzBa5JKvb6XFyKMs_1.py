
def get_primiera_score(deck):
  d = { "7" : 21, "6" : 18, "5" : 15, "4" : 14, "3" : 13, "2" : 12, "A" : 16, "K" : 10, "Q" : 10, "J" : 10}
  arr = [0,0,0,0]
  for c in deck:
    val = d[c[0]]
    if c[1] == 'd' and val > arr[0]: arr[0] = val
    elif c[1] == 'h' and val > arr[1]: arr[1] = val
    elif c[1] == 'c' and val > arr[2]: arr[2] = val
    elif c[1] == 's' and val > arr[3]: arr[3] = val
       
  if 0 in arr: return 0
  else : return sum(arr)

