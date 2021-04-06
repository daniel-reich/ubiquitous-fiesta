
import re
​
def evaluate_polynomial(poly, num):
    if '//' in poly:
        return 'invalid'
    
    poly = re.sub(r'(\d+)x', r'\1*x', poly)
    poly = re.sub(r'x', str(num), poly)
    poly = re.sub(r'(\d+\^\d+)', r'(\1)', poly)
    poly = re.sub(r'(\d+?)\(', r'\1*(', poly)
    poly = re.sub(r'\^', '**', poly)
    
    try:
        return int(eval(poly))
    except (TypeError, SyntaxError):
        return 'invalid'

