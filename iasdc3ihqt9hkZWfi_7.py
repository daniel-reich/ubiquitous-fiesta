
def can_give_blood(d, r):
  l=['O-','O+','B-','B+','A-','A+','AB-','AB+']
  h=['80','C0','A0','F0','88','CC','AA','FF']
  h=[list(bin(int(i,16))[2:].zfill(8)) for i in h]
  return int(h[l.index(r)][l.index(d)])

