
factor_sort=lambda n:sorted(sorted(n)[::-1],key=l)
​
l=lambda m:sum(-1 for i in range(1,m+1) if m%i==0)

