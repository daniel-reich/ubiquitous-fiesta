
def single_number(nums):
  s,s_more = set(),set()
  for n in nums:
    if n in s:
      s_more.add(n)
    s.add(n)
  return (s-s_more).pop()

