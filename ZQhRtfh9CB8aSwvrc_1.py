
greater_than_sum=lambda n:all(v>sum(n[:i]) for i,v in enumerate(n[1:],1))

