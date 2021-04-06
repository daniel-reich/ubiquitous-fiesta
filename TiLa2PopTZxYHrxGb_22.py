
def playback_duration(duration, speed):
    durationList = duration.split(":")
    alinanSaat = durationList[0]
    alinanDakika = durationList[1]
    alinanSaniye = durationList[2]
​
    saat = int(alinanSaat)
    dakika = int(alinanDakika)
    saniye = int(alinanSaniye)
​
    hesap = (saat * 3600 + dakika * 60 + saniye) // speed
​
    sonSaat = int((hesap // 3600))
    sonSaatStr = str(sonSaat)
    sonDakika = int(((hesap % 3600) // 60))
    sonDakikaStr = str(sonDakika)
    sonSaniye = int((hesap % 60))
    sonSaniyeStr = str(sonSaniye)
    
    if len(sonSaatStr) <= 1:
      sonSaatStrx = "0" + sonSaatStr
    else:
      sonSaatStrx = sonSaatStr
      
    if len(sonDakikaStr) <= 1:
      sonDakikaStrx = "0" + sonDakikaStr
    else:
      sonDakikaStrx = sonDakikaStr
  
    if len(sonSaniyeStr) <= 1:
      sonSaniyeStrx = "0" + sonSaniyeStr
    else:
      sonSaniyeStrx = sonSaniyeStr
    
    cevapStringi = sonSaatStrx +":"+ sonDakikaStrx +":"+ sonSaniyeStrx
      
    return cevapStringi

