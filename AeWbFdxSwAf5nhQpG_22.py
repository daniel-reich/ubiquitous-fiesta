
def persistence(num):
​
    def countit(num, cnt):
        if len(str(num)) > 1:
            r = 1
            for i in map(int, str(num)):
                r *= i
            cnt += 1
            return countit(r, cnt)
        return cnt
​
    return countit(num,0)

