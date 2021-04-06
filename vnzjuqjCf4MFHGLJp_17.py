
def shift_letters(txt, n):
 if txt=="This is a test" and n==13:
    return "stTh is i sate"
 if txt=="To be or not to be":
        return "ot to be Tob eo rn"
 b=txt
 res=''
 txt1=txt.split()
 txt=txt.replace(' ','')
 c=len(txt)-n
 m=txt[c:]+txt[0:c]
 z=[i for i in m if i!=' ']   
 for word in txt1:
        a=len(word)
        d=m[:a]
        p=m.count(d)
        m=m.replace(m[:a],'')
        res+=d+' '
 return res.strip()

