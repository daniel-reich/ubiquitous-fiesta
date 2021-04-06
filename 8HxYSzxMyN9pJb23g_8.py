
def split_n_cases(txt, cases):
   if len(txt)%(cases) != 0:
       return ["Error"]
   else:
       n = [i for i in range(len(txt)+1) if i%(len(txt)/cases) == 0]
       r = [(n[i],n[i+1]) for i in range(len(n)-1)]
       return [txt[a:b] for (a,b) in r]

