
def is_magic(square):
  line = sum(square,[])
  if set(line) != set(range(1,len(line)+1)):
    return False
  sums = [sum(l) for l in square] + \
           [sum(z) for z in zip(*square)] + \
           [sum(l[i] for i,l in enumerate(square)), \
            sum(l[len(square)-1-i] for i,l in enumerate(square))]
  return not square or len(set(sums)) == 1

