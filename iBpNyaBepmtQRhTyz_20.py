
def c_cipher(msg, keyword):
    condensedMsg = ""
    ciphTxt = ""
    sortedKeyword = ''.join(sorted(keyword))
    ciphTxtCol = []
    splitTxt = ""
    columnNums = ""
    deciphTxt = ""
    deciphTxtCol = [keyword for i in range(len(keyword))]
    count = 0
    if " " in msg:
        for i in msg:
            if i == " " or i == ".":
                continue
            else:
                condensedMsg += i.lower()
                
        for i in condensedMsg:
            splitTxt += i
            count += 1
            if count == len(keyword):
                count = 0
                ciphTxtCol.append(splitTxt)
                splitTxt = ""
                
        if count != 0:
            while count < len(keyword):
                splitTxt += "x"
                count += 1
            count = 0
            ciphTxtCol.append(splitTxt)
            
        for i in range(1, len(sortedKeyword)+1):
            count = 0
            for j in keyword:
                if sortedKeyword[i-1] == j:
                    break
                count += 1
            for k in ciphTxtCol:
                ciphTxt += k[count]
        return ciphTxt
    
    else:
        ciphTxt = msg
        for i in ciphTxt:
            splitTxt += i
            count += 1
            if count == len(ciphTxt)/len(keyword):
                count = 0
                ciphTxtCol.append(splitTxt)
                splitTxt = ""
        for i in range(1, len(sortedKeyword)+1):
            count = 1
            for j in keyword:
                if sortedKeyword[i-1] == j:
                    columnNums += str(count)
                    break
                count += 1
​
        sortedCiphTxtCol = [keyword for i in range(len(ciphTxtCol))]
​
​
        for i in range(len(columnNums)):
            sortedCiphTxtCol[int(columnNums[i])-1] = ciphTxtCol[i]
            
        for i in range(len(ciphTxt)//len(keyword)):
            for j in range(len(sortedCiphTxtCol)):
                deciphTxt += sortedCiphTxtCol[j][i]
        return deciphTxt

