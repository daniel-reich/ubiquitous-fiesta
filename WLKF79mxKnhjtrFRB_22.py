
def is_good_match(lst):
    n=0
    output=[]
    if len(lst)%2!=0:
        return "bad match"
    while n<len(lst):
        output.append(lst[n]+lst[n+1])
        n+=2
    return output

