
def diag_dom(arr):
    ans = True
    for i, li in enumerate(arr):
      target = abs(li.pop(i))
      sum_list = sum(list(map(abs, li)))
      if target <= sum_list:
        ans = False
    return ans

