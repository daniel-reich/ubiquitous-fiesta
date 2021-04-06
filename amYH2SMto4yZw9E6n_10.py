
def validate(s):
  l = len(s)
  if l == 11:
    return s[0] == "1" and s.isnumeric()
  if l == 12:
    return {s[3],s[7]} in [{"/"},{"-"},{"."},{" "}] and (s[0:3] + s[4:7] + s[8:12]).isnumeric()
  if l == 15:
    return s[0] == "+" and {s[2],s[6],s[10]} in [{"-"}] and (s[1:2]+s[3:6]+s[7:10]+s[11:15]).isnumeric()
  if l == 14:
    if s[0]+s[4:6]+s[9] == "() -":
      return (s[1:4]+s[6:9]+s[10:14]).isnumeric()
    return s[0] == "1" and {s[1],s[5],s[9]} in [{"/"},{"-"},{"."},{" "}] and (s[2:5] + s[6:9]+ s[10:14]).isnumeric()
  if l == 16:
    return s[0] == "1" and (s[1:3]+s[6:8]+s[11]) == " () -" and (s[3:6]+s[8:11]+s[12:16]).isnumeric()
  if l == 10:
    return s.isnumeric()
  return False

