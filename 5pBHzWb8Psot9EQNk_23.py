
def simple_encoder(s):
    return ''.join(list(map(lambda x:'[' if s.lower().count(x)==1 else ']',list(s.lower()))))

