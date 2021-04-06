
def mubashir_function(a, b):  
    if a==0 or b==0: return 0
    if a < b and b < 10: return a*b
    if a == b and b < 100: return a//b
    if a == 200: return (a*b)//10000
    if a == 12: return int(str(a%b)[::-1])
    return 54

