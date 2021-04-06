
import re
def swap_xy(string):                    # Swap X and Y coordinates
  arr = re.findall(r'(-?\d+)', string)
  return ", ".join(["("+arr[i+1]+", "+arr[i]+")" for i in range(0, len(arr)-1, 2)])

