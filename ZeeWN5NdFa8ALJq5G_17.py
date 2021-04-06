
from statistics import mean
def nearest_chapter(chapt, page):
  nums = sorted(chapt.values())
  chaps = sorted(chapt.keys(),key = lambda x: chapt[x])
  for i,chap in enumerate(nums):
    try:
      if page <= chap:
        avg = mean([nums[i-1],chap])
        return chaps[i] if page >= avg else chaps[i-1]
    except IndexError:
      if page <= nums[0]:
        return chaps[0]
  return chaps[-1]

