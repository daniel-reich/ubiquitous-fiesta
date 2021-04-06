
def base_conv(n, b):
    string, sol = "abcdefghijklmnopqrstuvwxyz", ""
    if str(n).isnumeric():
        while n:
            sol = string[n % b] + sol
            n //= b
        return sol
    else:
        dic = {string[i]:i for i in range(b)}
        for i in n:
            if i not in dic:
                return n+" is not a base "+str(b)+" number."
        sol, mult = 0, 1
        for i in n[::-1]:
            sol += dic[i]*mult
            mult *= b
        return sol

