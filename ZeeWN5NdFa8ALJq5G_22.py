
def nearest_chapter(chapt, page):
    keys_lis = sorted(list(chapt.keys()))
    mem_pg = [keys_lis[0],chapt[keys_lis[0]]]
    for key in keys_lis: 
        if chapt[key] >= page: 
            if chapt[key] - page<= page - mem_pg[1]: 
                return key
            else: 
                return mem_pg[0]
        mem_pg = [key,chapt[key]]

