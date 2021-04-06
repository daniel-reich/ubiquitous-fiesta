
def triangle(perimeter,area):
  limit = perimeter//2 + 1
  pos_val = []
  for i in range(1,limit):
    for j in range(1,i+1):
        k = perimeter-(i+j)
        m = max(i,j,k)
        if m<=(perimeter-m):  
          s=perimeter/2
          if area == round((s*(s-i)*(s-j)*(s-k))**0.5,5):
            temp = sorted([k,j,i])
            if pos_val.count(temp)==0:
              pos_val.append(temp)
  pos_val.sort(key=lambda x:x[0])
  return pos_val

