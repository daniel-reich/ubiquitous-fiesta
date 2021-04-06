
def recur_index(t,s=''):
  if t:
    if t[0]in s:return{t[0]:[s.index(t[0]),len(s)]}
    else:s+=t[0];return recur_index(t[1:],s)
  else:return{}

