
def arrow(num):
    ans = ['>' * i for i in range(1,num+1)]
    if len(ans[-1]) % 2 == 0:
        ans.extend(ans[::-1])
    else:
        ans.extend(ans[:-1][::-1])
    return ans

