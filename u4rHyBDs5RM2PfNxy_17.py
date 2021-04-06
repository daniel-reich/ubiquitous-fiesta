
def count_ones(lst):
    import re
    str1 = ''.join([str(item) for item in lst])    
    return len(re.findall('11+',str1))

