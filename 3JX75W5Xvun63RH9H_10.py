
def describe_num(n):
    desc = ['The most']
    descriptors = ['brilliant', 'exciting', 'fantastic',
                   'virtuous', 'heart-warming', 'tear-jerking',
                   'beautiful', 'exhilarating', 'emotional',
                   'inspiring']
    for i in range(10):
        if n%(i+1)==0:
            desc.append(descriptors[i])
    desc.append('number is {}!'.format(n))
    return ' '.join(desc)

