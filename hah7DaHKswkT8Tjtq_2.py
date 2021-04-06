
def separate_numbers(s):
    min_len = len(s)//2+1
    chk_num = str(10**min_len)
    while chk_num not in s and min_len>=1:
        chk_num = str(int(chk_num)//10)
        min_len = len(chk_num)
    if s.index(chk_num)>0:
        min_len -=1
    start, string, len_s = int(s[:min_len]), "", len(s)
    for i in range(start, start+5):
        if len(str(i)) + len(string) <= len_s:
            string += str(i)
    return "YES {}".format(s[:min_len]) if string == s and len(s)>1 else "NO"

