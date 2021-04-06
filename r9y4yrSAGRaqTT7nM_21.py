
find_missing=lambda l:sum(range(len(min(l,key=len)),len(max(l,key=len))+1))-sum(len(x)for x in l)if l and all(l)else 0

