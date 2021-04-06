
def pyramidal_string(string, _type):
    result = []
    i = 1
    y = []
    while len(string) > sum(y):
        y.append(i)
        i += 1
    if sum(y) != len(string): 
        return "Error!"
    if _type == "REV":
        string = string[::-1]   
    for i in range(len(y)):
        result.append(" ".join(list(string[: i + 1])))
        string = string[i + 1 : ]
    if _type == "REV": 
        return [x[::-1] for x in result[::-1]]
    return result

