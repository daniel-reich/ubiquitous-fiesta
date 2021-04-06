
def modify(astr):
    return convert_binary_to_number(convert_number_to_binary(join_array_and_convert_to_number(replaceLetterWithAlpha(reverse(astr)))))
​
​
​
​
​
​
​
def reverse(astr):
    return astr[::-1]
​
​
def replaceLetterWithAlpha(astr):
    alphabet = ' abcdefghijklmnopqrstuvwxyz'
    newlist = []
    astr = astr.lower()
    for eachletter in astr:
        newlist.append(str((alphabet.index(eachletter))))
    return newlist
​
​
def join_array_and_convert_to_number(alist):
    emptystring = ''.join(alist)
    return int(emptystring)
​
def convert_number_to_binary(anumber):
    return bin(anumber)[2:]
​
def convert_binary_to_number(binarynumber):
    return int(binarynumber)

