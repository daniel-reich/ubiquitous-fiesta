
def remove_virus(files):
    disk = files.replace('PC Files: ', '').split(', ')
    clean_files = []
​
    for i, f in enumerate(disk):
        if 'virus' in f:
            search = f.split('virus')
            if search[0] in ['not', 'anti']:
                clean_files.append(f)
        elif 'malware' not in f:
            clean_files.append(f)
​
    if not clean_files:
        return 'PC Files: Empty'
    return 'PC Files: ' + ', '.join(clean_files)

