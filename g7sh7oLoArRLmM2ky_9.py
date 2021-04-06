
def baconify(msg, mask=''):
    b = [['a','uuuuu'],['b','uuuul'],['c','uuulu'],['d','uuull'],['e','uuluu'],['f','uulul'],['g','uullu'],['h','uulll'],['i','uluuu'],['j','uluul'],['k','ululu'],['l','ulull'],['m','ulluu'],['n','ullul'],['o','ulllu'],['p','ullll'],['q','luuuu'],['r','luuul'],['s','luulu'],['t','luull'],['u','luluu'],['v','lulul'],['w','lullu'],['x','lulll'],['y','lluuu'],['z','lluul'],['.','llllu'],[' ','lllll']]
    msgL = []
    temp = ''
    m = ''
    if mask == '':
        msg = msg.replace(' ','')
        msg = msg.replace(':','')
        msg = msg.replace(',','')
        msg = msg.replace('.','')
        msg = msg.replace(';','')
        i = -1
        while i < len(msg)-1:   
            i += 1    
            if msg[i].isupper():
                temp += 'u'
            else:
                temp += 'l'
            if i % 5 == 4:    
                msgL.append(temp)
                temp = ''    
        for i in range(len(msgL)):
            for j in range(len(b)):
                if msgL[i] == b[j][1]:
                    m += b[j][0] 
        return m
    else:
        for i in range(len(msg)):
            for j in range(len(b)):
                if msg[i].lower() == b[j][0]:
                    msgL += b[j][1]        
        a = 0
        for i in range(len(mask)):
            if mask[i].isalpha() == False:
                m += mask[i]
            else:
                if a >= len(msgL):
                    m += mask[i].lower()
                elif msgL[a] == 'u':
                    m += mask[i].upper()
                else:
                    m += mask[i].lower()
                a += 1
             
        return m

