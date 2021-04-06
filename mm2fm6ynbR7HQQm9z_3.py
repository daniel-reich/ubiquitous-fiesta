
def knights_jump(square):
  a,b = s_to_coor(square)
  ans = []
  for i,j in [[1,2],[2,1],[-1,2],[-2,1],[1,-2],[2,-1],[-1,-2],[-2,-1]]:
    x,y = a+i,b+j
    if 0<=x<8 and 0<=y<8:
      ans.append(coor_to_s((x,y)))
      
  return ','.join(sorted(ans, key = lambda s:s[::-1]))
  
​
st = 'ABCDEFGH'
​
s_to_coor = lambda s: (st.index(s[0]), int(s[1])-1)
​
coor_to_s = lambda t: st[t[0]] + str(t[1]+1)

