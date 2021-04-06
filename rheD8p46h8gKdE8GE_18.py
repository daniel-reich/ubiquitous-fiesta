
def grayscale(lst):
  lst= [[[255 if i>255 else i for i in j] for j in k] for k in lst]
  lst= [[[0 if i<0 else i for i in j] for j in k] for k in lst]
  return [[[round(sum(j)/3) for i in j] for j in k]for k in lst]

