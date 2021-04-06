
def alpha_clash(str_A, ind_A, str_Z, ind_Z):
  left_A = [ord(l) for i,l in enumerate(str_A) if i not in ind_Z]
  left_Z = [ord(l) for i,l in enumerate(str_Z) if i not in ind_A]
  scores = [left_A[i]-left_Z[i] for i in range(16)]
  return {'A':sum(s for s in scores if s>0), 'Z':-sum(s for s in scores if s<0)}

