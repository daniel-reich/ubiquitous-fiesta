
def countdown(n,st):
    s = []
    for i in range(1,n+1):
        s+=[str(i)+'.'+' ']
    return ''.join(s[::-1])+st.upper()+'!'

