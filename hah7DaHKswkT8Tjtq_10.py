
def separate_numbers(s):
    for i in range(0, len(s)//2):
        sb = ""
        num1 = int(s[:i+1])
        while len(sb) < len(s):
            sb += str(num1)
            num1 += 1
        if sb == s:
            return "YES "+ s[:i+1]
    return "NO"

