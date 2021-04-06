
def can_exit(lst):
    if lst[4][6]==1: return False
    m,n,loopc,confloop=0,0,0,0
    while m <(len(lst)):
     while n <(len(lst[0])):
        if m == 4 and n == 6:return True
        if (m<4) and (lst[m+1][n]==0) and (n<6) and (lst[m][n+1]==0):
          confloop+=1
          a,b=m,n
          if loopc==0:n=n+1
          else:m=m+1
          break
        elif (n<6) and (lst[m][n+1] == 0):
          n=n+1
          break
        elif (m<4) and (lst[m+1][n]==0):
          m=m+1
          break
        elif confloop>5:return False
        else:
          if confloop>0:
            loopc+=1
            m,n=a,b
          else:return False

