
def edabit_in_string(string):
    find = "edabit"
    word2make = []
    if "edabit" in string:
        return "YES"
    else:
        for j in range(len(find)):
            for i in range(len(string)):
                if string[i] == find[j]:
                    word2make.append(string[i])
                    string = string[i+1:]
                    break
        if "".join(word2make) == find:
            return "YES"
        else:
            return "NO"

