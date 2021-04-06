
nearest_chapter=lambda c,p:min(c,key=lambda x:(abs(p-c.get(x)),-c.get(x)))

