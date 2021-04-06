
def calculate_arrowhead(lst):
    ans = sum(list(map(lambda x: len(x) if x.startswith('>') else -len(x),lst)))
    return  '>'*ans if ans>0 else '' if ans==0 else '<'*(abs(ans))

