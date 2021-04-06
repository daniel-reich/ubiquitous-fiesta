
def generate_palindromes(limit):
    ans = []
    for x in range(limit+1,0,-1):
        if len(ans) == 15:
            break
        elif str(x) == str(x)[::-1]:
            ans.append(x)
    return ans[::-1]

