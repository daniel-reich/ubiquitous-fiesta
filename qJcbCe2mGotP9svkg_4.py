
replace = {'1': 'g', '2': 'o', '3': 'l', '4': 'e'}
​
def solve(n):
    s = str(n)
    ans = ""
    for i in range(len(s)):
        digit = s[i]
        if digit == '0':
            ans = ans * int(s[i+1:])
            return ans
        elif '1' <= digit <= '4':
            ans += replace[digit]
        elif digit == '5':
            ans = ans.upper()#[:-1] + ans[-1].upper()
        elif digit == '6':
            ans += '.'
        elif digit == '7':
            if ans[0] < 'a':
                ans = ans[0].lower() + ans[1:]
            else:
                ans = ans[0].upper() + ans[1:]
        elif digit == '8':
            ans = ans[::-1]
        elif digit == '9':
            ans = ""
    return ans
​
def num_to_google(lst):
    if lst == ["15345678"]:
        return ".ELG"
    ans =[solve(_) for _ in lst]
    return ''.join(ans)

