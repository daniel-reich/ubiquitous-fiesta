
import math
​
lengthes = [n * (n + 1) // 2 for n in range(101)]
​
def pyramidal_string(string, _type):
    L = len(string)
    if L not in lengthes:
        return "Error!"
    if L == 0:
        return []
    if L == 1:
        return [string]
    ans = []
    if _type == "REG":
        cur = 1
        while len(string) > 0:
            ans.append(' '.join([c for c in string[:cur]]))
            string = string[cur:]
            cur += 1
    else:
        cur = int(round(-.5 + math.sqrt(.25 + 2 * L), 0))
        while len(string) > 0:
            ans.append(' '.join([c for c in string[:cur]]))
            string = string[cur:]
            cur -= 1
    return ans

