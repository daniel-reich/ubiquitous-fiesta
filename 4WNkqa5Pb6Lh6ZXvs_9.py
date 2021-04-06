
import re
​
def format_mul(s):
    if s[-1]=='x' and s[-2].isdigit():
        return s[:-1]+'*'+'x'
    elif (s[-2]=='x' or s[-2]==')' or s[-2].isdigit())and s[-1]=='(':
        return s[:-1]+'*'+s[-1]
    else:
        return s
​
def format_text(text, n):
    text = re.sub(r'([\d.]+x)', lambda x: format_mul(x.group()),text)
    text = re.sub(r'[x\)\d]+\(', lambda x: format_mul(x.group()),text)
    text = re.sub(r'\^', "**",text)
    text = re.sub(r'x', str(n),text)
    
    return text
​
def evaluate_polynomial(text, n):
    length = len(text)
    if length == 0:
        return "invalid"
    
    count = 0
    valid_set = {'(',')','*','^','+','-','/','x'}
    for i in range(length):
        if (not text[i].isdigit()) and text[i] not in valid_set:
            return "invalid"
        if (i+1) <= (length-1):
            if text[i] == '/' and text[i+1] == '/':
                return "invalid"
    
    for i in range(length):
        if text[i] == '(':
            count += 1
        elif text[i] == ')':
            count = count -1
        if count < 0:
            return "invalid"
    if count != 0:
        return "invalid"
    
    text = format_text(text,n)
    #print(text)
​
    return eval(text)

