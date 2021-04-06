
def happiness_number(s):
  d = {":)":1, "(:":1, ":(":-1,"):":-1}
  return sum([d[s[i:i+2]] for i in range(len(s)-1) if s[i:i+2] in d.keys()])

