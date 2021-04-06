
def Kaprekar(n, count=1, iterations=''):
​
    # include repdigits restrictions
    repdigits = [1111, 2222, 3333, 4444, 5555, 6666, 7777, 8888, 9999]
    if n in repdigits:
        return (
        '\n---------- The Mysterious Number 6174 ----------\n' +
        '\nError, n cannot be a repdigit.' +
        '\n' +
        '\n------------------------------------------------')
​
    # add leading zeros if n does not have 4 digits
    if len(str(n)) == 1:
        n = str(n).zfill(4)
    elif len(str(n)) == 2:
        n = str(n).zfill(4)
    elif len(str(n)) == 3:
        n = str(n).zfill(4)
    else:
        n = str(n)
​
    # arrange the digits in ascending and then in descending order to get two four-digit numbers.
    digits = []
    for i in str(n):
        i = int(i)
        digits.append(i)
​
    a = sorted(digits)
    d = sorted(digits, reverse=True)
    
    a_str = ''
    for i in a:
        a_str += str(i)
    a_str = a_str.zfill(4)
    a_num = int(''.join(a_str))
​
    d_str = ''
    for i in d:
        d_str += str(i)
    d_str = d_str.zfill(4)
    d_num = int(''.join(d_str))
​
    # subtract the smaller number from the bigger number
    check = d_num - a_num
    iterations_seq = 'Iteration Nr. ' + str(count) +': '+ d_str + ' - ' + a_str + ' = ' + str(check).zfill(4) + '\n'
​
    # check the result and if 6174 is not reached iterate again
    if check == 6174:
        return (
        '\n---------- The Mysterious Number 6174 ----------\n' +
        '\nNumber of iterations: ' + str(count) + '\n' +
        '\nIterations:\n' +
        '\n' +
        str(iterations) +
        str(iterations_seq) +
        '\n------------------------------------------------')
    else:
        return Kaprekar(check, count+1, iterations+iterations_seq)

