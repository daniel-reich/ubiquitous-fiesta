
import re
​
def text_to_num(phone):
    phone = re.sub(r'[A-C]','2' , phone)
    phone = re.sub(r'[D-F]', '3', phone)
    phone = re.sub(r'[G-I]', '4', phone)
    phone = re.sub(r'[J-L]', '5', phone)
    phone = re.sub(r'[M-O]', '6', phone)
    phone = re.sub(r'[P-S]', '7', phone)
    phone = re.sub(r'[T-V]', '8', phone)
    phone = re.sub(r'[W-Z]', '9', phone)
    return phone

