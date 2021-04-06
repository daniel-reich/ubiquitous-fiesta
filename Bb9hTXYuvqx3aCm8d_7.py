
def alpha_clash(str_A, ind_A, str_Z, ind_Z):
  lst_A = [i for n, i in enumerate(str_A) if n not in ind_Z]
  lst_Z = [i for n, i in enumerate(str_Z) if n not in ind_A]
  score_A = sum([ord(i) - ord(j) for i, j in zip(lst_A, lst_Z) 
                if ord(i) > ord(j)])
  score_Z = sum([ord(i) - ord(j) for i, j in zip(lst_Z, lst_A) 
                if ord(i) > ord(j)])
  return {'A': score_A, 'Z': score_Z}

