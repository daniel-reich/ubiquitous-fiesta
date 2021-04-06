
def slicer(string, s):
    if string == s:
        return "[:]"
    elif string == s[::-1]:
        return "[::-1]"
    elif len(s) == 1:
        return str([string.index(s)])
    elif s in string:
        if s[0] == string[0]:
            return "["+":"+str(string.index(s[-1])+1)+"]"
        elif s[-1] == string[-1]:
            return "["+str(string.inded(s[0]))+":]"
        else:
            return "["+str(string.index(s[0]))+":"+str(string.index(s[-1])+1)+"]"
    elif string.index(s[0])<string.index(s[1]):
        step = string.index(s[1])-string.index(s[0])
        if step <= len(string[string.index(s[-1])+1:]) and s[0] != string[0]:
            return "["+str(string.index(s[0]))+":"+str(string.index(s[-1])+1)+":"+str(step)+"]"
        elif step > len(string[string.index(s[-1])+1:]) and s[0] != string[0]:
            return "["+str(string.index(s[0]))+"::"+str(step)+"]"
        elif step > len(string[string.index(s[-1])+1:]) and s[0] == string[0]:
            return "[::"+str(step)+"]"
    elif string.index(s[0])>string.index(s[1]):
        step = string.index(s[-1])-string.index(s[-2])
        if s[-1] == string[0] and string[-1] == s[0]:
            return "[::"+str(step)+"]"
        elif s[-1] != string[0] and string[-1] == s[0]:
            return "[:"+str(string.index(s[-1])-1)+":"+str(step)+"]"
        elif s[-1] != string[0] and string[-1] != s[0] and step <= len(string[string.index(s[::-1][-1]):])*-1:
            return "["+str(string.index(s[0]))+"::"+str(step)+"]"
        else:
            return "["+str(string.index(s[0]))+":"+str(string.index(s[-1])-1)+":"+str(step)+"]"

