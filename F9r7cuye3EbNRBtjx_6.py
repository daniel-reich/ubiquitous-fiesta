
def find_bracket_pair(A):
    closing = [i for i in range(len(A)) if A[i] == ']']
    for end in closing:
        start = end - 1
        while start >= 0 and A[start] != ']':
            if A[start] == '[':
                return start, end
            start -= 1            
    return -1, -1
​
def string_builder(s):
    A = []
    chars = ""
    num = ""
    for c in s:
        if not c.isnumeric() and c not in "[]":
            chars += c
        else:
            if chars != "":
                A.append(chars)
                chars = ""
            if c.isnumeric():
                num += c
            else:
                if num != "":
                    A.append(int(num))
                    num = ""
                A.append(c)
    if chars != "":
        A.append(chars)
    if num != "":
        A.append(int(num))
    while True:
        start, end = find_bracket_pair(A)
        if start >= 0:
            if end - start > 2:
                for i in range(start + 2, end):
                    A[start+1] += A[i]
                    A[i] = ""
            mult = A[start-1]
            A = A[:start-1] + [A[start+1] * mult] + A[end+1:]
        else:
            break
    return ''.join(A)

