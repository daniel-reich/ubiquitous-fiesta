
larger_than_right=lambda l:[l[i]for i in range(len(l)-1)if l[i]>max(l[i+1:])]+[l[-1]]

