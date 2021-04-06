
def face_interval(n):
  return ":/" if type(n)!=list else ":)" if max(n)-min(n) in n else":("

