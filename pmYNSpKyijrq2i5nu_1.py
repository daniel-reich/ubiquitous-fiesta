
def darts_solver(sections, darts, target):
  def rec(sections, darts, target):
    if darts==0 and target==0: return [[]]
    if darts==0 or not sections or target<0: return []
    take = [[sections[0]]+x for x in rec(sections, darts-1, target-sections[0])]
    skip = rec(sections[1:], darts, target)
    return take + skip
  def fmt(subset):
    return '-'.join(map(str, subset))
  return list(map(fmt, rec(sections, darts, target)))

