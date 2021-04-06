
single = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
          'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
teens = {'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14,
         'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18,
         'nineteen': 19}
tens = {'ten': 10, 'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50,
        'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90}
​
def eng2nums(s):
    lst = s.split()
    res = 0
    if 'hundred' in lst:
        res += single[lst[0]] * 100
        lst = lst[2:]
    if lst:
        if lst[0] in teens:
            res += teens[lst[0]]
        elif lst[0] in tens:
            res += tens[lst[0]]
            if len(lst) > 1:
                res += single[lst[1]]
        elif lst[0] in single:
            res += single[lst[0]]
    return res

