
import itertools as it
clean_up=lambda f,s:[list(g)for k,g in it.groupby(f,key=lambda x:x.split('.')[(1,0)[s[0]=='p']])]

