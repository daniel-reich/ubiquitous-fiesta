
def secret_password(pw):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
​
    if not(pw.isalpha() and pw.islower() and len(pw) == 9):
        return "BANG! BANG! BANG!"
​
    # divide into three parts
    pw1, pw2, pw3 = pw[:3], pw[3:6], pw[6:]
​
    # convert 1st & 3rd letter of pw1 to indx # in alpha
    ch = pw1[:1]
    pre = str(alpha.index(ch) + 1 % 26)
    ch = pw1[2:]
    post = str(alpha.index(ch) + 1 % 26)
    pw1 = pre + pw[1:2] + post
​
    # reverse 4th,5th and 6th chars
    pw2 = pw2[::-1]
​
    # replace 7,8,9 with next letter in alpha
    temp = pw3[:]
    pw3 = ""
    for ch in temp:
        i = (alpha.index(ch) + 1) % 26
        pw3 += alpha[i]
​
    # return string in this order 
    return pw2+pw3+pw1

