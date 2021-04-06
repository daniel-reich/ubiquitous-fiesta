
def bw_transform(text):
    a=''
    lst=sorted([text[i:]+text[:i] for i in range(len(text))])
    for i in range(len(lst)):
        a+=lst[i][-1]
    return a

