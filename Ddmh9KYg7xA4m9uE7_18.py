
def convert_binary(str1):
    return "".join([str(0) if ord(i) <=109 else str(1) for i in str1.lower()])

