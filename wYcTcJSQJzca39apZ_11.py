
def truncate(t,l):r=t[:l].split();return" ".join([r,r[:-1]][t[l].isalpha()])if l<len(t)else t

