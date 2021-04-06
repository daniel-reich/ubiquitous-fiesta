
def ulam(n):
    arr,i,st = [1,2],3,set([1,2])
    while len(arr) < n:
        cnt = 0
        for j in range(len(arr)):
            if i-arr[j] in st and arr[j] != i-arr[j]:
                cnt += 1
            if cnt > 2:
                break
        if cnt == 2:
            arr.append(i)
            st.add(i)
        i += 1
    return arr[-1]

