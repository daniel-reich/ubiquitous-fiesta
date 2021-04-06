
def spartans_cipher(message, n_Slide):
    l = len(message)
    if l % n_Slide > 0:
        a = l // n_Slide + 1
    else:
        a = l // n_Slide
    b = a*n_Slide-l
    message += b*' '
    myans = ''
    for i in range(a):
        for j in range(i,l+b,a):
            myans += message[j]
​
    return myans.rstrip()

