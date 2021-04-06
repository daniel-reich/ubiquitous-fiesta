
def encrypt(word):
#Step 1: Reverse the input: "elppa"
    rword = word[::-1]
    rword = rword.replace('a','0')
    rword = rword.replace('e','1')
    rword = rword.replace('o','2')
    rword = rword.replace('u','3')
    rword = rword+'aca'
      
    return rword

