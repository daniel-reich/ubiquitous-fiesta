
def find_longest(s):
    low = s.split()
    first = get_word(low[0])
    if len(low) == 1:
        return first
    return max(first, find_longest(' '.join(low[1:])), key=len)  
​
def get_word(s):
    s = s.replace("'s", '')
    ans = ''
    for x in s:
        if x.isalpha():
            ans += x
    return ans.lower()

