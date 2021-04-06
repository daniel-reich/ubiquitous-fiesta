
def get_lucky_number(size, nth):
    kacinci=1
    sonuc=0
    my_list=list(range(1,size+1))
    while sonuc==0:
        new_array=silme(my_list,kacinci,sonuc,nth)
        my_list=new_array[0]
        sonuc = new_array[1]
        kacinci = new_array[2]
    return sonuc
    
def silme(liste,kacinci,sonuc,nth):
    setyet=False
    yeniliste=[]
    for i in range(0,len(liste)):
        if i>=len(liste):
            break
        if (kacinci>len(liste)):
            sonuc=liste[nth-1]
            break
        if i>0 and liste[i]>kacinci and not setyet:
            kacinci=liste[i]
            setyet=True
        if (i+1)%kacinci or i==0:
            yeniliste.append(liste[i]) 
    return [yeniliste,sonuc,kacinci]

