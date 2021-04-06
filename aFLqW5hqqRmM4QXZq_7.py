
def bar_chart(results):
    s = sorted(sorted([(k, v) for k, v in results.items()], key=lambda x: x[0]), reverse=True, key=lambda x: x[1])
    rs = ''.join([s[i][0] + "|" + "#"*int(s[i][1]/50) + " " + str(s[i][1]) + "\n" if s[i][1] > 0 else s[i][0] + "|"+ str(s[i][1]) + "\n" for i in range(len(s))])
    return rs[:len(rs)-1]

