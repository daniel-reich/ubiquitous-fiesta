
def is_early_bird(_range, n):
  s=''.join(str(i) for i in range(_range+2))
  a=[list(range(i,i+len(str(n)))) for i in range(len(s)) if s.startswith(str(n),i)]
  return a+['Early Bird!']*(a[0][0]<s.find(str(n)+str(n+1)))

