
def join(lst):
    result = [str(lst[0]), []]
    for word in lst[1:]:
        l = len(result[0])
        counter = 0
        print(result[0])
        for i in range(0,len(word)):
            if word[:i+1] ==result[0][len(result[0])-len(word[:i+1]):]:
                result[0] += word[i+1:]
                result[1].append(len(word)-len(word[i+1:]))
                break
        if l == len(result[0]) and word not in result[0]:
            result[0] += word
    if len(result[1]) == 0:
        return [result[0], 0]
    return [result[0], min(result[1])]

