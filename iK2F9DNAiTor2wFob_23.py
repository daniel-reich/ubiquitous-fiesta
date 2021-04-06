
def calc(s):
    s_ascii = "".join(([str(ord(char)) for char in s]))
    s_ascii_modified = s_ascii.replace('7', '1')
    s_ascii = sum([int(i) for i in s_ascii])
    s_ascii_modified = sum([int(i) for i in s_ascii_modified])
​
    return s_ascii - s_ascii_modified

