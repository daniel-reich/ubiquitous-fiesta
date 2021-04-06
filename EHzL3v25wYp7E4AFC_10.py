
def can_build(s1, s2):
  while s2!='':
    if not s2[0] in s1:return False
    s1,s2=s1.replace(s2[0],'',1),s2[1:]
  return True

