
def bit_rotate(n, m, d):
    if d:
        m= m%n.bit_length()
        
        number = 2**m -1
        
        a = ((((n&number) << (n.bit_length())) | n) >> m)
​
        return a
    else:
       bits = 2**(n.bit_length())-1
       return (n<<m | n>>(n.bit_length()-m)) & bits

