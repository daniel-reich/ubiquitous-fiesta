
def is_triplet(n1, n2, n3):
      ln=list([n1,n2,n3])
      ln.sort()
      if ln[0]*ln[0]+ln[1]*ln[1]==ln[2]*ln[2]:
            return True
      return False

