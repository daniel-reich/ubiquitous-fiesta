
def remove_virus(pc_files):
  all_files = pc_files.split()[2:]
  good_files = [file.strip(',') for file in all_files if 'malware' not in file and
                ('virus' not in file or 'antivirus' in file or 'notvirus' in file)]
  return 'PC Files: {}'.format(', '.join(good_files) if good_files else 'Empty')

