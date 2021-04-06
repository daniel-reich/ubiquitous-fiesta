
def split_and_delimit(txt, num, delimiter):
  ans = ''
  for i in range(0,len(txt),num):
    ans += txt[i:i+num] + delimiter
  return ans[:-1]

