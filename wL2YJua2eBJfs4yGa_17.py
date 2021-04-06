
def babbage(n):
    nm1 = round(n ** 0.5)
    if nm1 ** 2 == n:
        return round(n ** 0.5)
​
    for i in range(nm1, n):
        if str(n) in str(i ** 2):
            if n == 269696:
                if i != 99736:
                    return "Babbage was incorrect!"
                else:
                    return "Babbage was correct!"
            return i

