
def markdown(symbol):
    def foo(st,pattern):
        words = st.split()
        for i in range(len(words)):
            if pattern.lower() in words[i].lower():
                words[i] = symbol + words[i] + symbol
        return ' '.join(words)
    return foo

