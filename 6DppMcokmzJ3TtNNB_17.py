
import re
​
def true_alphabetic(txt):
    length = [len(word) for word in txt.split()]
    order_txt = "".join(sorted(re.sub(r" ", "", txt)))
    print(order_txt)
    start = 0
    result = ""
    end = 0
    for num in length:
        end += num
        result += order_txt[start:end] + " "
        start += num
    return result.rstrip()

