
def fib_str(n, st):
    while len(st) < n:
        st.append(st[-1] + st[-2])
    return ', '.join(x for x in st)

