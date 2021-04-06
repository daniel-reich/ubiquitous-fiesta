
def letter_combinations(digits):
    aplh_index = [[],[],["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"], ["j", "k", "l"], ["m", "n", "o"], ["p", "q", "r", "s"],["t", "u", "v"], ["w", "x", "y", "z"]]
    length = 1
    for i in digits:
        length *= len(aplh_index[int(i)])
    results = []
    count = 0
    for i in range(len(digits)):
        result = ["" for i in range(length)]
        for char in aplh_index[int(digits[i])]:
            forward = (length // len(aplh_index[int(digits[i])])) * (aplh_index[int(digits[i])].index(char) + 1)
            while count != length:
                result[count] += char
                count += 1
                if count == forward:
                    break
        if len(result[-1]) != "":
            count = 0
            results.append(result)
            length = length // len(aplh_index[int(digits[i])])
    
    result = results[0]
    results.pop(0)
    for i in range(len(results)):
        needmore = len(result) // len(results[i])
        results[i] = results[i] * needmore
​
    for o in results:
        for i in range(len(result)):
            result[i] += o[i]
​
    return result

