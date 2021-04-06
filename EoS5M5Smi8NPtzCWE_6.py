
def secret(text):
  ans = text[0:-2]
  ans1 = int(text[-1])
  main_ans = '<{0}></{0}>'.format(ans)
  return main_ans * ans1

