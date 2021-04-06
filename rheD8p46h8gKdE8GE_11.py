
grayscale=lambda l:[[[round(sum(((y,0)[y<0],255)[y>255]for y in x)/3)]*3for x in z]for z in l]

