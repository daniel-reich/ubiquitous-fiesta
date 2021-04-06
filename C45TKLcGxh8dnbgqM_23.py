
def caesar_cipher(s, k):
    s = list(s)
    while not k < 26:
        k -= 26
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = upper.lower()
    for i in range(len(s)):
        if s[i] in upper:
            s[i] = upper[upper.index(s[i]) + (k - (26 if upper.index(s[i]) + k > 25 else 0))]
        elif s[i] in lower:
            s[i] = lower[lower.index(s[i]) + (k - (26 if lower.index(s[i]) + k > 25 else 0))]
    return "".join(s)

