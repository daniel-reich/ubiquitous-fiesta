
is_shifted=lambda l,m: len(set(m[i]-l[i] for i in range(len(l))))==1
is_multiplied=lambda l,m: len(set(m[i]/l[i] for i in range(len(l))))==1

