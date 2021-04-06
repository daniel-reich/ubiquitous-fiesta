
def sort_contacts(names, sort):
    return sorted(names or [], key=lambda x:x.split()[1], reverse=sort!='ASC')

