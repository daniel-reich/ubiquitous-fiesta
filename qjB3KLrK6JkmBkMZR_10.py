
def can_capture(queens):
  l=[[ord(list(i)[0])-64,int(list(i)[1])] for i in queens]
  return abs(l[0][0]-l[1][0])==abs(l[0][1]-l[1][1]) or l[0][0]==l[1][0] or l[0][1]==l[1][1]

