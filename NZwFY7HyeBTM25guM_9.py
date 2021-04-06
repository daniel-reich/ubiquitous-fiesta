
import re
def convert_to_decimal(perc):
    num = re.findall('\d*\.?\d+', "".join(perc))
    answer = []
    
    for i in num:
        if "." in i:
            answer.append(float(i)/100)
        else:
            answer.append(int(i)/100)
​
    return answer

