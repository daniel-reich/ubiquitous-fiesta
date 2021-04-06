
def lengthen(string,input):
    longest=max([string,input],key=len)
    
    shortest=min([string,input],key=len)
    i,s=divmod(len(longest),len(shortest))
    output=shortest*i+shortest[:s]
    return output

