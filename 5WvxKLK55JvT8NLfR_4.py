
diag_dom=lambda l:not any(2*abs(l[i][i])<=sum(abs(x)for x in l[i])for i in range(len(l)))

