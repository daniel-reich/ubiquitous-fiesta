
def mathematical (exp, numbers):
    
    results =[] 
    ext_lst = []
    
    if '+'in exp:
        for i in numbers: 
            results.append(i + int(exp[-1])) 
            
    elif '^' in exp:
        for i in numbers:
            results.append(i ** int(exp[-1])) 
            
    elif 'x' in exp:
        for i in numbers:
            results.append(i * int(exp[-1])) 
    elif '-' in exp:
        for i in numbers:
            results.append(i - int(exp[-1]))
    elif '/' in exp:
        for i in numbers:
            results.append(int(i / int(exp[-1])))
            
    for j in range(len(numbers)):
        ext_lst.append("f({})={}".format(numbers[j], results[j]))
    
    return ext_lst

