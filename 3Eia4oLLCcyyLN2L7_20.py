
def remove_repeats(s):
    ans = s[0]
    for x in range(1,len(s)):
        if s[x] != s[x-1]:
            ans += s[x]
    return ans

