
digits_count=lambda n:0if(n<1and n>0)or n>-1and n<0else 1+digits_count(n/10if n else n-.5)

