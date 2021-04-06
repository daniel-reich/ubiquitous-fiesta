
def find_and_remove(dct):
  final = {}
  for i in dct:
    final[i] = {j:int(dct[i][j]) for j in dct[i] if all(k.isdigit() for k in dct[i][j])}
  return final

