
def split_and_delimit(string,num,char):
    return char.join([string[a:a+num] for a in range(0,len(string),num)])

