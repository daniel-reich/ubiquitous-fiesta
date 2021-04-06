
def stmid(string):
 lst = string.split()
 return ''.join([lst[i][0] if len(lst[i]) % 2 == 0 else lst[i][int(len(lst[i])/2)] for i in range(len(lst))])

