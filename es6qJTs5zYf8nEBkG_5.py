
def is_rectangle(coordinates):
    if len(coordinates)!=4:
        return False
    s=set(())
    for i in coordinates:
        for j in range(len(i)):
            if i[j].isnumeric():
                if i[j-1]=='-':
                    n=-int(i[j])
                else:
                    n=int(i[j])
                s.add(n)
    if len(s)==4:
        return True
    return False

