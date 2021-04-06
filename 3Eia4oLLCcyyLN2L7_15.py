
def remove_repeats(s):
  return"".join(s[i].replace(s[i],"")if s[i]==s[i+1]else s[i]for i in range(len(s)-1))+s[-1]

