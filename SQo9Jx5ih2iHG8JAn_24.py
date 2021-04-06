
def expanded_form(num):
    ans = ''
    num = str(num)
    length = len(num)-1
    for i in range(len(num)):
        if num[i]!='0':
            if i !=0: ans+=' + '
            ans+=num[i]+(length-i)*'0'
    return ans

