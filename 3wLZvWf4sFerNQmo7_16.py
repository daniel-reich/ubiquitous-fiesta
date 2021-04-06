
def neutralise(s1, s2):
  ans=""
  for i in range(len(s1)):
    if s1[i]!=s2[i]:
      ans+="0"
    elif s1[i]=="+":
      ans+="+"
    else:
      ans+="-"
  return ans

