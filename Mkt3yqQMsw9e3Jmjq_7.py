
def disjoint_cycle_form(per):
  ans, n= set(), len(per)
  for i in range(n):
    if all(i not in cyc for cyc in ans):
      if per[i] !=i:
        cyc = (i,per[i])
        while per[cyc[-1]] != i:
          cyc += (per[cyc[-1]],)
        ans = ans.union({cyc})
  return ans

