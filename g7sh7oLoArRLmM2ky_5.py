
def baconify(msg, *mask):
    code='uuuuu-uuuul-uuulu-uuull-uuluu-uulul-uullu-uulll-uluuu-uluul-ululu-ulull-ulluu-ullul-ulllu-'
    code+='ullll-luuuu-luuul-luulu-luull-luluu-lulul-lullu-lulll-lluuu-lluul-llllu-lllll'
    punc=',:;?.! '
    if mask==():
        for i in punc:
            msg=msg.replace(i,'')
        p=0
        new=''
        for i in msg:
            if i.isalpha():
                p+=1
                if p%5==0:
                    new+=msg[p-5:p]+' '
        new=new.split()
        ans=''
        for i in new:
            dec=''
            for j in i:
                if j.isupper():
                    dec+='u'
                else:
                    dec+='l'
            x=chr(code.find(dec)//6+97)
            if x=='{':x='.'
            if x=='|':x=' '
            ans+=x
        return ans
    else:
        p=0
        msg=msg.lower()
        mask=str(mask[0]).lower()
        for i in msg:
            dec=6*(ord(i)-97)
            cw=code[dec:dec+5]
            if i=='.':cw='llllu'
            if i==' ':cw='lllll'
            for j in cw:
                m=mask[p]
                while m in punc:
                    p+=1
                    m=mask[p]
                if j=='u':
                    mask=mask[:p]+m.upper()+mask[p+1:]
                p+=1
    return mask

