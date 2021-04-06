
def ave_spd(t, s1, s2):
  t1 = t/60 ; d1=d2=s1*t1 ; t2 = d2/s2
  return int((d1+d2)/(t1+t2))

