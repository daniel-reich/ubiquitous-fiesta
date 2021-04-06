
def slicer(s,t):
  A=[s.find(x) for x in t]
  if len(A)==1:
    return '[{}]'.format(A[0])
  else:
    d=A[1]-A[0]
    if d==1:
      if A[0]==0:
        if A[-1]==len(s)-1:
          return '[:]'
        else:
          return '[:{}]'.format(A[-1]+1)
      else:
        if A[-1]==len(s)-1:
          return '[{}:]'.format(A[0])
        else:
          return '[{}:{}]'.format(A[0], A[-1]+1)
    else:
      if d>1:
        if A[0]==0 or A[0]==len(s)-1:
          if A[-1]==len(s)-1 or A[-1]-d<0 or A[-1]+d>=len(s):
            return '[::{}]'.format(d)
          else:
            return '[:{}:{}]'.format(A[-1]+1, d)
        else:
          if A[-1]==len(s)-1 or A[-1]-d<0 or A[-1]+d>=len(s):
            return '[{}::{}]'.format(A[0],d)
          else:
            return '[{}:{}:{}]'.format(A[0], A[-1]+1, d)
      else:
        if A[0]==0 or A[0]==len(s)-1:
          if A[-1]==len(s)-1 or A[-1]+d<0 or A[-1]-d>=len(s):
            return '[::{}]'.format(d)
          else:
            return '[:{}:{}]'.format(A[-1]-1, d)
        else:
          if A[-1]==len(s)-1 or A[-1]+d<0 or A[-1]-d>=len(s):
            return '[{}::{}]'.format(A[0],d)
          else:
            return '[{}:{}:{}]'.format(A[0], A[-1]-1, d)

