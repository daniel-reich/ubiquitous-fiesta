
def gcd(m, n):
    while n != 0:
        t = n
        n = m%n
        m = t
    return m
​
import re
def fractions(text):
    parts = re.findall(r'[0-9.]+',text)
​
    zeros_before = len(parts[0]) - 1 - parts[0].find('.')
    
    int_part = int(parts[0][:parts[0].find('.')])
    
    if zeros_before != 0:
        dec_part_up = int(parts[0][parts[0].find('.')+1:])
        dec_part_down = int(10**zeros_before)
    else:
        dec_part_up = 0
        dec_part_down = 1
    
    part1_len = len(parts[1])
    x = int(parts[1])
    
    x_deno = int((10**part1_len - 1)*(10**zeros_before))
    
    inter_up = x*dec_part_down+dec_part_up*x_deno
    inter_down = dec_part_down*x_deno
    
    gcd_num = gcd(inter_up,inter_down)
    
    final_down = inter_down//gcd_num
    final_up = inter_up//gcd_num + int_part*final_down
    
    result = str(final_up)+'/'+str(final_down)
    
    return result

