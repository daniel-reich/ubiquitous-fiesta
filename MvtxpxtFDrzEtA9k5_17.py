
def palindrome_descendant(num):
    if len(str(num)) == 1:
        return False
    elif str(num) == str(num)[::-1]:
        return True
    else:
        reduce = []
        i = 0
        while i < (len(str(num))-1):
            reduce.append(str(int(str(num)[i]) + int(str(num)[i+1])))
            i += 2
        reduce = int(''.join(reduce))
        return palindrome_descendant(reduce)

