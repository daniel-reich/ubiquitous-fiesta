
def bit_rotate(n,m,d):
  bin_num = bin(n)[2:]
  liste,indexes,final_indexes,final_bit = [],[],[],[]
  compteur = 0
  [liste.append(_) for _ in bin_num]
  for _ in liste:
    if _ == "1":
      indexes.append(compteur)
    compteur+=1
​
  [final_indexes.append((int(i)+m)%len(bin_num)) if d == True else final_indexes.append((int(i)-m)%len(bin_num)) for i in indexes]
  [final_bit.append("1") if _ in final_indexes else final_bit.append("0") for _ in range(len(bin_num))]
​
  return(int("".join(final_bit),base=2))

