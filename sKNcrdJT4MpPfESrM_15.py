
def remove_virus(files):
    files = files.replace(',', '').split()[2:]
    clean_files = []
    for file in files:
        if "antivirus" in file or "notvirus" in file or \
            ("virus" not in file and "malware" not in file):
            clean_files.append(file)
    return "PC Files: Empty" if len(clean_files) == 0 else "PC Files: " + ", ".join(clean_files)

