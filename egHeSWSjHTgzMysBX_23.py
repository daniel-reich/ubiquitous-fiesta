
def half_a_fraction(fract):
  s=list(map(int,fract.split("/")))
  return "/".join(map(str,[s[0]//2 if s[0]%2==0 else s[0],s[1] if s[0]%2==0 else s[1]*2]))

