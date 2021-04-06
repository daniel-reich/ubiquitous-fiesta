
def longest_slide(s):
    for i in range(1, len(s)):
        l = []
        for ii in range(len(s[i])):
            if ii == 0:
                l.append(s[i-1][0] + s[i][ii])
            elif ii == len(s[i]) - 1:
                l.append(s[i-1][-1] + s[i][ii])
            else:
                l.append(max(s[i-1][ii-1:ii+1]) + s[i][ii])
        s[i] = l
    return max(s[-1])

