
def get_quartiles(lst, method):
    x=sorted(lst)
    gey=[]
    if method=="T":
        gey.append(x[0])
        if len(x)%2!=0:
            ge=int(len(x)-1)
            gi=int((len(x)-1)/2)
            he=ge-int(gi)
            cd=x[he]
        elif len(x)%2==0:
            ge = int(len(x) - 1)
            gi = int((len(x) - 1) / 2)
            gii=int((len(x) ) / 2)
            he = [ge - int(gi)]+[ge-int(gii)]
            howa=x[he[1]]
            miami=x[he[0]]
            if howa !=miami:
                cd=(howa+miami)/2
                if int(cd)==cd:
                    cd=int(cd)
            elif howa==miami:
                cd=howa
        if int(len(str(he)))==1:
            c=x[:he+1]
            while c:
                if int(len(c))==1:
                    gaeil=c[0]
                    gey.append(gaeil)
                    gey.append(cd)
                    break
                elif int(len(c))==2:
                    nunu = c[0]
                    ww = c[1]
                    gaeil = (int(nunu) + int(ww)) / 2
                    gey.append(gaeil)
                    gey.append(cd)
                    break
                c.pop(0)
                c.pop()
            cec=x[he:]
            while cec  :
                if int(len(cec)) == 1:
                    gaeil = cec[0]
                    gey.append(gaeil)
                    break
                elif int(len(cec)) == 2:
                    nunu = cec[0]
                    ww = cec[1]
                    gaeil = (int(nunu) + int(ww)) / 2
                    gey.append(gaeil)
                    break
                cec.pop(0)
                cec.pop()
            coolist=int(len(x))
            gey.append(coolist)
        elif int(len(he))==2:
            c=x[:he[0]]
            while c:
                if int(len(c))==1:
                    gaeil=c[0]
                    gey.append(gaeil)
                    gey.append(cd)
                    break
                elif int(len(c)) == 2:
                    nunu=c[0]
                    ww=c[1]
                    gaeil=(int(nunu)+int(ww))/2
                    gey.append(gaeil)
                    gey.append(cd)
                    break
                c.pop(0)
                c.pop()
            cec=x[he[1]+1:]
            while cec:
                if int(len(cec))==1:
                    gaeil=cec[0]
                    gey.append(gaeil)
                    break
                elif int(len(cec)) == 2:
                    nunu=cec[0]
                    ww=cec[1]
                    gaeil=(int(nunu)+int(ww))/2
                    gey.append(gaeil)
                    break
                cec.pop(0)
                cec.pop()
            coolist = int(len(x)-1)
            gey.append(x[coolist])
    elif method=="MM":
        gey.append(x[0])
        if len(x) % 2 != 0:
            ge = int(len(x) - 1)
            gi = int((len(x) - 1) / 2)
            he = ge - int(gi)
            cd = x[he]
        elif len(x) % 2 == 0:
            ge = int(len(x) - 1)
            gi = int((len(x) - 1) / 2)
            gii = int((len(x)) / 2)
            he = [ge - int(gi)] + [ge - int(gii)]
            howa = x[he[1]]
            miami = x[he[0]]
            if howa != miami:
                cd = (howa + miami) / 2
                if int(cd) == cd:
                    cd = int(cd)
            elif howa == miami:
                cd = howa
        if int(len(str(he))) == 1:
            c = x[:he]
            while c:
                if int(len(c)) == 1:
                    gaeil = c[0]
                    gey.append(gaeil)
                    gey.append(cd)
                    break
                elif int(len(c)) == 2:
                    nunu = c[0]
                    ww = c[1]
                    gaeil = (int(nunu) + int(ww)) / 2
                    gey.append(gaeil)
                    gey.append(cd)
                    break
                c.pop(0)
                c.pop()
            cec = x[he+1:]
            while cec:
                if int(len(cec)) == 1:
                    gaeil = cec[0]
                    gey.append(gaeil)
                    break
                elif int(len(cec)) == 2:
                    nunu = cec[0]
                    ww = cec[1]
                    gaeil = (int(nunu) + int(ww)) / 2
                    gey.append(gaeil)
                    break
                cec.pop(0)
                cec.pop()
            coolist = int(len(x))
            gey.append(coolist)
        elif int(len(he)) == 2:
            c = x[:he[0]]
            while c:
                if int(len(c)) == 1:
                    gaeil = c[0]
                    gey.append(gaeil)
                    gey.append(cd)
                    break
                elif int(len(c)) == 2:
                    nunu = c[0]
                    ww = c[1]
                    gaeil = (int(nunu) + int(ww)) / 2
                    gey.append(gaeil)
                    gey.append(cd)
                    break
                c.pop(0)
                c.pop()
            cec = x[he[1]+1:]
            while cec:
                if int(len(cec)) == 1:
                    gaeil = cec[0]
                    gey.append(gaeil)
                    break
                elif int(len(cec)) == 2:
                    nunu = cec[0]
                    ww = cec[1]
                    gaeil = (int(nunu) + int(ww)) / 2
                    gey.append(gaeil)
                    break
                cec.pop(0)
                cec.pop()
            coolist = int(len(x)-1)
            gey.append(x[coolist])
    elif method=="MS":
        gey.append(x[0])
        if len(x)%2!=0:
            ge=int(len(x)-1)
            gi=int((len(x)-1)/2)
            he=ge-int(gi)
            cd=x[he]
        elif len(x)%2==0:
            ge = int(len(x) - 1)
            gi = int((len(x) - 1) / 2)
            gii=int((len(x) ) / 2)
            he = [ge - int(gi)]+[ge-int(gii)]
            howa=x[he[1]]
            miami=x[he[0]]
            if howa !=miami:
                cd=(howa+miami)/2
                if int(cd)==cd:
                    cd=int(cd)
            elif howa==miami:
                cd=howa
        if int(len(x))==6:
            gey.append(x[1])
            gey.append(cd)
            gey.append(x[4])
            gey.append(x[5])
        else:
            hello=int(len(x)+1)
            soit=hello/4
            c = str(soit)
            f = c.split(".")
            f1 = str(f[1])
            f2 = str("0.")
            f3 = f2 + f1
            if float(f3) >= 0.5:
                cc = int(f[0]) + 1
            elif float(f3) <= 0.4:
                cc = int(f[0]) + 0
            gey.append(cc)
            gey.append(cd)
            soite = (hello*3) / 4
            print(soite)
            c = str(soite)
            f = c.split(".")
            f1=str(f[1])
            f2=str("0.")
            f3=f2+f1
            if float(f3) >= 0.6:
                cc = int(f[0]) + 1
            elif float(f3) <= 0.5:
                cc = int(f[0]) + 0
            gey.append(cc)
            coolist = int(len(x) - 1)
            gey.append(x[coolist])
    return(gey)

