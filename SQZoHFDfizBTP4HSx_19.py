
from collections import Counter
def missing_alphabets(txt):
    result = ''
    cnt_txt = Counter(txt)
    max_occurrence = max(cnt_txt.values())
    for i in range(97, 123):
        if chr(i) not in cnt_txt:
                   result += chr(i) * max_occurrence
        elif cnt_txt[chr(i)] < max_occurrence:
                   print(chr(i))
                   result += chr(i) * (max_occurrence - cnt_txt[chr(i)])
    return result

