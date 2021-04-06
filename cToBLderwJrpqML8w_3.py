
champions=lambda d:max(d,key=lambda x:(x['wins']*3+x['draws'],x['scored']-x['conceded']))['name']

