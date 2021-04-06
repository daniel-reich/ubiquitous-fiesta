
def jumping_frog(n, S):
  def f(i):
    if i < 0 or i < n and S[i] < 0: return 2 * n
    if i >= n: return 0
    d = S[i]
    S[i] = -1
    return 1 + min((f(i + d), f(i - d)))
  r = 1 + f(0)
  return [r,'no chance :-('][r > 2 * n]

