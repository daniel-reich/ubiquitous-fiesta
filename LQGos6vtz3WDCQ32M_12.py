
def Kaprekar(num):
    output = ""
    min_list, max_list, val_list = [],[],[]
    output = report('header')
    if repdigit(str(num)):
        output += report('repdigit')
        output += report('footer')
        return output
    val = int(standardize(str(num), front=False))
    i = 0
    while val != 6174:
        i += 1
        v_min, v_max = minmax(val)
        val = v_max - v_min
        min_list.append(standardize(str(v_min)))
        max_list.append(standardize(str(v_max)))
        val_list.append(standardize(str(val)))
        val = int(standardize(str(val), front=False))
    output += report('results', min_list,max_list,val_list,i)
    output += report('footer')
    return output
​
# checks for repeating digits (1111). 
def repdigit(n):
    num = str(n)
    if len(num) == 4:
        if (num[0] == num[1] == num[2] == num[3]):
            return True
    return False
​
# add '0' padding to front or back of number.
def standardize(num_str, front= True):
    val = ''
    length = 4 - len(num_str)
    val = '0'*length
    if front:
        return val + num_str
    else:
        return num_str + val
​
# returns min & max values for n. 
def minmax(n):
    num = str(n)
    sort_ascending = sorted(num)
    n_min = ''.join(sort_ascending)
    sort_descending = sorted(num, reverse=True)
    n_max = ''.join(sort_descending)
    return int(n_min),int(n_max)
​
# generates output report. 
def report(cmd, min_lst=[],max_lst=[],val_lst=[],iters=0):
    if cmd == 'header':
        return '\n' + '-'*10 + " The Mysterious Number 6174 " + '-'*10 + "\n\n"
    elif cmd == 'repdigit':
        return "Error, n cannot be a repdigit.\n"
    elif cmd == 'footer':
        return '\n'+"-"*48
    elif cmd == 'results':
        results = ""
        results = "Number of iterations: " + str(iters) + '\n\n' +          \
                  "Iterations:" + '\n\n'
        for i in range(iters):
            results += "Iteration Nr. " + str(i+1) + ': ' + max_lst[i]     \
            + ' - ' + min_lst[i] + ' = ' + val_lst[i] + '\n'
        return results

