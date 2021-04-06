
def even_odd_transform(lst, n):
  final = []
  for num in lst:
    if num%2:final.append(num+(2*n))
    else:final.append(num-(2*n))
  return final

