
def complete_bracelet(lst):
 for x in range(2,len(lst)):
    if lst[0]==lst[x]:
        if lst[0:x]==lst[x:2*x]:
            print(len(lst[2*x:]))
            if len(lst[2*x:])%len(lst[0:x])==0:return True
 return False

