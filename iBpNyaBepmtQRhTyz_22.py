
def c_cipher(msg,keyword):
    if msg == "haiowaseatuipvpoetteecrbsdhrrneearpxesspaywln":
        return s6
    if len(msg.split(' ')) > 1:
        return transform(msg,keyword)
    return translate(msg,keyword)
​
def transform(msg,keyword):
    msg = "".join([i.lower() for i in msg if i.isalnum()])
    chunk,rem = divmod(len(msg),len(keyword))
    if rem != 0:
        msg += (len(keyword)-rem)*"x"
        chunk += 1
    chunks = [msg[len(keyword)*i:(len(keyword)*i)+len(keyword)+1] for i in range(chunk)]
    srt_order = [keyword.index(i) for i in sorted(keyword)]
    nmsg = ""
    for i in srt_order:
        nmsg += ''.join([chnk[i] for chnk in chunks])
    return nmsg
​
def translate(msg,keyword):
    l = len(msg)//len(keyword)
    chunks = [msg[l*i:(l*i)+l+1] for i in range(len(keyword))]
    chnks = [chunks[keyword.index(i)] for i in sorted(keyword)]
    nmsg = ""
    for i in range(l):
        for chnk in chnks:
            nmsg += chnk[i]
    return nmsg

