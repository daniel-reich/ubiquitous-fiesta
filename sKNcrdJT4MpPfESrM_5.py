
def remove_virus(files):
    good = [f for f in files[10:].split(', ')
            if f in ['antivirus.exe', 'notvirus.exe']
            or not (f[:-4].endswith('virus')
            or f[:-4].endswith('malware')
            or f == '')]
    return 'PC Files: ' + (', '.join(good) if good else 'Empty')

