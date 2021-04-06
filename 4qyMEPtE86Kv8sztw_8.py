
def binary_sum(nums):
    def base10(n):
        a = n.split(".") [0][::-1]
        b = n.split(".") [1]
​
        b10 = 0
​
        d = 1
​
        for x in range(len(b)):
            d *= 2
            if b [x] == "1":                   
                b10 += 1/d
​
        d = 0
​
        for x in range(len(a)):
            if a [x] == "1":
                b10 += 2**d
            d += 1
​
        return b10
​
    n1 = base10(nums [0])
    n2 = base10(nums [1])
​
    sum = float(n1) + float(n2)
​
    i = str(sum).split(".")[0]
    d = str(sum).split(".")[1]
​
    if i == "0":
        i = ""
    elif not d == "0":
        i += " "
​
    if not d == "0":
        top = int(d)
        bot = 10**len(d)
​
        for x in reversed(range(top+1)):
            if bot % x == 0 and top % x == 0:
                bot /= x
                top /= x
                break
​
        fra = str(int(top)) + "/" + str(int(bot))
​
        i += fra
​
    if i == "":
        i = "0"
​
    return i

