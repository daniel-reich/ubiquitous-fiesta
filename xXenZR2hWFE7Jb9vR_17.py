
is_isomorphic=lambda s,t:all(s.find(x)==t.find(y)for x,y in zip(s,t))

