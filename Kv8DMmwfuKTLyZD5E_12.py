
def make_dartboard(n):
    result = ["1"*n]
    if n%2 == 0:
        for i in range(2,int(n/2)+1):
            result.append(result[-1][:i-1]+str(i)*(n-(len(result[-1][:i-1])*2))+(result[-1][:i-1])[::-1])
        return [int(i) for i in result+result[::-1]]
    else:
        for i in range(2,n//2+2):
            result.append(result[-1][:i-1]+str(i)*(n-(len(result[-1][:i-1])*2))+(result[-1][:i-1])[::-1])
        return [int(i) for i in result+result[:-1][::-1]]

