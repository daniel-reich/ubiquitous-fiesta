
import re
def trouble(num1, num2):
    matches1,matches2=re.search(r'(\d)\1{2}',str(num1)),re.findall(r'(\d)\1{1}',str(num2))  
    return(bool(matches1 and matches2) and (list(set(matches1.group(0)))[0] in matches2))

