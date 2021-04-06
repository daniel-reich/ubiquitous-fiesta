
def complete_square(arr):
  r, c = len(arr), len(arr[0])
  h_pad, v_pad = max(r-c,0), max(c-r,0)
  
  return [row + [0]*h_pad for row in arr] + [[0]*c]*v_pad

