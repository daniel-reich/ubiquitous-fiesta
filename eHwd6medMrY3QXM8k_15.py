
def is_consecutive(s):
    count = 1
    while count <= len(s)//2:
        lst = [int(s[i:i+count]) for i in range(0, len(s), count)]
        l = []
        first = None
        for i in range(1, len(lst)):
            if not first:
                if lst[i] - lst[i - 1] == 1:
                    first = 0
                else:
                    first = 1
            if first == 0:
                if lst[i] - lst[i - 1] == 1:
                    l.append(True)
                else:
                    l.append(False)
            else:
                if lst[i-1] - lst[i] == 1:
                    l.append(True)
                else:
                    l.append(False)
        if all(l):
            return True
        count += 1
    return False

