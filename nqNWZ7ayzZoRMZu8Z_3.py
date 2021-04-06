
avg_note=lambda s:[{'name':x['name'],'avgNote':round(sum(x['notes'])/len(x['notes']))if len(x['notes'])>0else 0}for x in s]

