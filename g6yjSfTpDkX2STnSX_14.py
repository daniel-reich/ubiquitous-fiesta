
def convert_to_hex(txt):
    st = ''
    for a in txt:
        st += ' ' + hex(ord(a))[2:]
    return st.lstrip().rstrip()

