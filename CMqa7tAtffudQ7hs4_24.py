
def sorting_steps(lst):
    ans=[];f=1;arr=lst[:]
    while f==1:
        f=0
        for i in range(len(arr)-1):
            if arr[i+1]<arr[i]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
                ans.append((i,i+1))
                f=1
    return ans

