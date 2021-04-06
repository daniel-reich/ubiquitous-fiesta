
def separate_numbers(s):
    lengths = [i+1 for i in range(len(s)//2)]
    for i in lengths:
        string = ''
        num = int(s[:i])
        for j in range(num,num + len(s)//i):
            string += str(j)
        if string[:len(s)] == s:
            return 'YES {}'.format(num)    
    return 'NO'

