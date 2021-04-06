
def get_name(address):
    n = address.split("@")[0]
    ans=""
    for i in n:
        if i.isalpha():
            ans+=i
    return ans

