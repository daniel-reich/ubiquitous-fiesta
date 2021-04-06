
import re
​
s = r'!"#$%&()*+,-./:;<=>?@\[\]^_{|}\\\''
all_in = (r'(?=.*[a-z])(?=.*[A-Z])(?=.*[\d])(?=.*['
          + s + r'])[a-zA-Z\d' + s + r']')
invalid = (r'(^.{,5}$|^.{31,}$|^(?=.*[ \t\n]).{6,30}$|^(?!.*[a-z]).{6,30}$|'
           + r'^(?!.*[A-Z]).{6,30}$|^(?!.*[\d]).{6,30}$|'
           + r'^(?!.*[' + s + r']).{6,30}$)')
weak = (r'(^' + all_in + r'{6,15}$|'
        + r'^(?!(.*[a-z]){3,})' + all_in + r'{16,30}$|'
        + r'^(?!(.*[A-Z]){3,})' + all_in + r'{16,30}$|'
        + r'^(?!(.*[\d]){3,})' + all_in + r'{16,30}$|'
        + r'^(?!(.*[' + s + r']){3,})' + all_in + r'{16,30}$)')
strong = (r'^(?=(.*[a-z]){3,})(?=(.*[A-Z]){3,})(?=(.*[\d]){3,})'
          + r'(?=(.*[' + s + r']){3,})[a-zA-Z\d' + s + r']{16,30}$')

