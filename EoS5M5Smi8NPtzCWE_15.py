
def secret(text):
    data = text.split("*")
    ans = ("<" + data[0] + ">" + "</" + data[0] + ">")*int(data[1])
    return ans

