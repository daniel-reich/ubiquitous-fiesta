
def maxmin(n):
  ns = [n] + [int(swap(list(str(n)), i, j)) for i in range(len(str(n))) for j in range(i)]
  ns = [x for x in ns if len(str(x)) == len(str(n))]
  return max(ns), min(ns)
def swap(L, i, j):
  L[i], L[j] = L[j], L[i]
  return "".join(L)

