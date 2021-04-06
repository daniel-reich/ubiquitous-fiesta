
import re
def swap_xy(txt):
  nums = [int(x) for x in re.findall('-?[0-9]+',txt)]
  j = str([tuple(nums[:2][::-1]), tuple(nums[2:][::-1])])
  return j.strip('[]')

