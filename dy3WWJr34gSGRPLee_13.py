
def make_box(n):
    if n>=2:
        output=[]
        output.append('#'*n)
        mystring=''
        mystring=mystring+'#'+' '*(n-2)+'#'
        for i in range(n-2):
            output.append(mystring)
        output.append('#'*n)
        return output
    else: return ['#']

