
def secret(text):
    tag, num = text.split("*")
    return ("<" + tag + ">" + "</" + tag + ">")*int(num)

