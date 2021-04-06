
def first_repeat(chars):
    for i in range(len(chars)):
        for j in range(len(chars)):
            if chars[i] == chars[j] and i != j:
                print(chars[j])
                return chars[j]
    return "-1"

