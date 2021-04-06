
def palindrome_descendant(num):
    while len(str(num))>=2:
        if str(num)[:len(str(num))//2] == str(num)[:-len(str(num))//2 -1:-1]:
            return True
        i = 0
        a = []
        while i < len(str(num))-1:
            tup = (int(str(num)[i]),int(str(num)[i+1]))
            a.append(str(sum(tup)))
            i += 2
        num = "".join(a)
        print(num)
    if len(str(num)) == 1:
        return False

