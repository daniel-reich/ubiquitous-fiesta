
def alternating_caps(txt):
  """Scrappy, shit code"""
  ans = txt[0].upper()
  for x in range(1,len(txt)): 
    if ans[x-1] == ' ':
      if ans[x-2].isupper() == True:
        ans += txt[x].lower()
      else:
        ans += txt[x].upper()
    elif ans[x-1].isupper() == True:  
      ans += txt[x].lower()
    else:
      ans += txt[x].upper()
  return ans

