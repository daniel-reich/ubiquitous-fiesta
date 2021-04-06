
def unstretch(word):
    output=word[0]
    for i in range(1,len(word)):
        if word[i]!=output[-1]:
            output=output+word[i]
    return output

