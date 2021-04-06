
def all_about_strings(txt):
    aset = set()
    retStr = ""
    index = -1
    length_of_str = len(txt)
    first_char = txt[0]
    last_char = txt[-1]
​
    if length_of_str % 2 != 0:
        middle_char = txt[length_of_str//2]
    else:
        middle_char = txt[length_of_str//2 - 1]
        middle_char += txt[length_of_str//2]
​
    for i in range(len(txt)):
        if txt[i] not in aset:
            aset.add(txt[i])
        else:
            index = i
            break
​
    if index == -1:
        retStr = "not found"
    else:
        retStr = "@ index " + str(index)
​
    return([length_of_str, first_char, last_char, middle_char, retStr])
​
#print(all_about_strings('LASA'))
print(all_about_strings('programming'))

