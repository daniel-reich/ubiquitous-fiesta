
def helper(lst):
  cur,m,cnt = lst[0],1,1
  for i in lst[1:]:
    if i == cur+1:
      cnt += 1
      if cnt > m:
        m = cnt
    else:
      cnt = 1
    cur = i
  return m
def longest_run(lst):
  return max(helper(lst),helper(lst[::-1]))

