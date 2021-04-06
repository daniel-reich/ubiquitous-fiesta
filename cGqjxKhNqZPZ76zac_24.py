
def fire(m, c):
   return "splash" if m[ord(c[0]) - 65][int(c[1]) - 1] == "." else "BOOM"

