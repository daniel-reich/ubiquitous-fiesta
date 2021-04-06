
def print_all_groups():
    numlst=["1","2","3","4","5","6"]
    txtlst=["a","b","c","d","e"]
    ans=[]
    for i in numlst:
        for j in txtlst:
            ans.append(i+j)
    return ", ".join(ans)

