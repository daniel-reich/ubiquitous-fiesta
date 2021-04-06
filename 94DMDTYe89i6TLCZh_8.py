
l="C# C++ Java JavaScript PHP Python Ruby Swift".split()
get_languages=lambda n:[l[i]for i in range(8)if(n//2**i)%2]

