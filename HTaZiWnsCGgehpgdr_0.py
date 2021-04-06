
def license_plate(s, n):
    s = s.replace("-", "").upper()
    remainder = len(s) % n
    returnString = ""
    for charIndex in range(0, len(s)):
        if charIndex < remainder-1:
            returnString+=s[charIndex]
        elif charIndex == remainder-1 and remainder != 0:
            returnString+=s[charIndex]+"-"
        elif (charIndex + 1 - remainder) % n == 0 and charIndex != len(s)-1:
            returnString+=s[charIndex]+"-"
        else:
            returnString+=s[charIndex]
​
    return returnString

