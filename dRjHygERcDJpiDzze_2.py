
def lengthen(s1, s2):
    if len(s1)<len(s2):
        num1=len(s2)%len(s1)
        num2=len(s2)//len(s1)
        return s1*num2+s1[0:num1]
    else:
        num1=len(s1)%len(s2)
        num2=len(s1)//len(s2)
        return s2*num2+s2[0:num1]

