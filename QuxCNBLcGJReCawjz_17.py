
def palindrome_type(n):
    binary =  str(bin(n).replace("0b",""))
    rebin = binary[::-1]
    renum = str(n)[::-1]
    num = str(n)
    if num == renum and  binary != rebin:
        return "Decimal only."
    elif num != renum and binary == rebin:
        return "Binary only."
    elif num == renum and binary == rebin:
        return "Decimal and binary."
    else:
        return "Neither!"

