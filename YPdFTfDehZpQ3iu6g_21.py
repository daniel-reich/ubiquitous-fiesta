
def roman_numerals(arg):
    r_to_i = {'I': '1', 'V': '5', 'X': '10', 'L': '50', 'C': '100', 'D': '500', 'M': '1000'}
    i_to_r = {'1': 'I', '5': 'V', '10': 'X', '50': 'L', '100': 'C', '500': 'D', '1000': 'M'}
    if isinstance(arg, str):
        # roman to integer
        result = 0
        arg = list(map(lambda elm: int(r_to_i.get(elm)), arg))
        for idx in range(len(arg)-1):
            a, b = arg[idx], arg[idx+1]
            result += a if a >= b else -a
        return result + arg[-1]
    else:
        # integer to roman
        arg = [int(elm) for elm in str(arg)][::-1]
        return ''.join(map(lambda elm: ''.join(map(lambda e: i_to_r.get(str(e)), elm)), map(lambda elm, p: [int(d) * 10**p for d in elm][::-1], map(lambda elm: "1"*elm if elm < 4 and elm > 0 else "15" if elm == 4 else "5" + "1"*(elm - 5), arg), range(len(arg)))))[::-1]

