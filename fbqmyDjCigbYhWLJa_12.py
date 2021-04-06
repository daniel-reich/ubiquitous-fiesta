
def split_into_buckets(phrase, n):
    string = phrase.split(' ')
    result = []
    temp = ''
    for i in range(len(string)):
        if len(string[i])<=n and len(temp)==0:
            temp = string[i]
        elif len(string[i])<=n and (len(temp)+len(string[i])+1)<=n:
            temp = temp + ' ' + string[i]
        elif len(string[i])<=n and (len(temp)+len(string[i])+1)>=n:
            result.append(temp)
            temp = string[i]
    if temp !='' and temp !='by':
        result.append(''.join(temp))
    return result

