
def res_series(resistors):
    return str(sum(resistors))
​
def res_parallel(resistors):
    sum_rec = 0.0
    for r in resistors:
        sum_rec += 1/r
    return str(round(1/sum_rec, 1))
​
​
def helper(schem, equivalent):
    n = len(schem)
    stack = []
    for i in range(n):
        if schem[i] == "(" or schem[i] == "[":
            stack.append((schem[i], i))
        if schem[i] == ')' or schem[i] == ']':
            substr = schem[stack[-1][1]: i+1]
​
            # parse resistors
            resistors = []
            start = 1
            for x in range(1, len(substr)):
                if substr[x] == ',':
                    resistors.append(float(substr[start:x]))
                    start = x + 1
            resistors.append(float(substr[start:x]))
​
            if schem[i] == ')':
                repl = res_series(resistors)
            else:
                repl = res_parallel(resistors)
            schem = schem.replace(substr, repl, len(substr))
            equivalent.append(schem)
            break
​
    if schem[0] == '(' or schem[0] == '[':
        helper(schem, equivalent)
​
def resist(schem):
    equivalent = []
    helper(schem, equivalent)
    return float(equivalent[-1])

