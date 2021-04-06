
def switcheroo(txt):
  A=txt.split()
  B=[]
  if txt=='':
    return ''
  else:
    for i in A:
      if i[-3:]=='nce' or (i[-4:-1]=='nce' and i[-1] in '/&%.,!;:)([]=?+#'):
        B.append(i.replace('nce','nts'))
      elif i[-3:]=='nts' or (i[-4:-1]=='nts' and i[-1] in '/&%.,!;:)([]=?+#'):
        B.append(i.replace('nts','nce'))
      else:
        B.append(i)
    for i,n in enumerate(A[-1]):
      if n in '/&%.,!;:)([]=?+#':
        if A[-1][i-3:i]=='nce':
          B[-1]=(A[-1].replace('nce','nts'))
        elif A[-1][i-3:i]=='nts':
          B[-1]=A[-1].replace('nts','nce')
    return ' '.join(B)

