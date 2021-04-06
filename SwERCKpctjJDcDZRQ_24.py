
def longest_string(str1, str2):
    stringy=str1+str2
    stringy=''.join(sorted(list(set(stringy))))
    return stringy

