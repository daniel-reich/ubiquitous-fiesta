
def num_to_google(lst):
    result = []
    for element in lst:
        element = str(element)
        if "9" in element:
            continue
        for i in range(len(element)):
            if element[i] == "0":
                result.append(result[-1]*int(element[i:]))
                result.pop(-2)
                break
            elif element[i] == "1":
                result.append("g")
            elif element[i] == "2":
                result.append("o")
            elif element[i] == "3":
                result.append("l")
            elif element[i] == "4":
                result.append("e")
            elif element[i] == "5":
                result[-1] = result[-1].upper()
            elif element[i] == "6":
                result.append(".")
            elif element[i] == "7":
                result[0] = result[0].swapcase()
            elif element[i] == "8":
                result = result[::-1]
    return "".join(result)

