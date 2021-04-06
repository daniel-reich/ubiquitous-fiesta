
def index(x,st,si):
    if x >= st+si:
        return (x - si)
    else:
        return x
size = 26
start = 65
alpha = [chr(start+i) for i in range(0,size)]
board = [[chr(index(start+i+j,start,size)) for i in range(0,size)] for j in range(0,26)]    
def vigenere(text, keyword):
    cypher = 0
    new_text = ""
    key = ""
    k = 0
    code = ""
    for i in range(0,len(text)):
        space = 0
        uppercase = 0
        for j in range(0,size):
            if text[i] == ' ' or text[i] == "'" or text[i] == '.':
                space = 1
            if text[i] == alpha[j]:
                uppercase = 1
        if space == 0: 
            if uppercase == 1:
                new_text += text[i]
            if uppercase == 0:
                new_text += chr(ord(text[i])-32)
            if k >= len(keyword):
                k -= len(keyword)
            key += chr(ord(keyword[k])-32)
            k += 1
        if new_text == text:
            cypher = 1
    if cypher == 0:
        for i in range(0,len(new_text)):
            for j in range(0,size):
                if new_text[i] == board[0][j]:
                    y = j
            for j in range(0,size):
                if key[i] == board[j][0]:
                    x = j
            code += board[x][y]
        return code
    if cypher == 1:
        for i in range(0,len(text)):
            for j in range(0,size):
                if key[i] == board[j][0]:
                    x = j
            for j in range(0,size):
                if text[i] == board[x][j]:
                    y = j
            code += board[0][y]
        return code

