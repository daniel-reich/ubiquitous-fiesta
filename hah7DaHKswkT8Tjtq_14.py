
def separate_numbers(s):
    if len(s) > 1:
        a_len = 1
        for i in range(len(str(int(s)//2))):
            a_start = 0
            a_end = a_start + a_len
            a = s[a_start:a_end]
            num = a
            b_len = len(str(int(a)+1))
            b_start = a_end
            b_end = b_start + b_len
            b = s[b_start:b_end]
            while int(b) == int(a) + 1:
                a_start = b_start
                a_end = b_end
                a = s[a_start:a_end]
                b_len = len(str(int(a)+1))
                b_start = a_end
                b_end = b_start + b_len
                if len(s) - a_end == 0:
                    return 'YES {}'.format(num)
                elif len(s) - (b_end) >= 0:
                    b = s[b_start:b_end]
                else:
                    break
            a_len += 1
            if a_len == len(s):
                break                
    return 'NO'

