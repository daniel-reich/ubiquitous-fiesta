
def max_occur(text):
    res = { (char,text.count(char)) for char in text if text.count(char)>1}
    if len(res)==0 :return "No Repetition"
    m = max(list(map(lambda x:x[1],res)))
    res =list(filter(lambda x:x[1]==m, list(res)))
    return sorted(list(map(lambda x:x[0],res)) )

