
def identify(*cube):
  length = [len(i) for i in cube]
  missing = sum([max(length)-i for i in length])
  IsFull = missing==0 and len(length)==length[0]
  return "Missing {}".format(missing) if missing>0 else "Full" if IsFull else "Non-Full"

