
super_digit=f=lambda n,k=1:f(sum(map(int,str(int(n)*k))))if int(n)>9else n

