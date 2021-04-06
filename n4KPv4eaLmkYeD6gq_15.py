
def face_interval(n):
  return ':{}'.format('/' if type(n)!=list else ')' if max(n)-min(n) in n else '(')

