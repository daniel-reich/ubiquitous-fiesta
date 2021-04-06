
def alphabet_index(st):
    return ' '.join(str(ord(ch)-96) for ch in st.lower() if ch.isalpha())

