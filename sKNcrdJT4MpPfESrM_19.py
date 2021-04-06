
def remove_virus(files):
  nFile = (files.replace("PC Files:","")).split(",")
  for i in nFile:
      if i.find("virus") != -1:
          if i.find("antivirus") != -1  or i.find("notvirus") != -1:
              pass
          else:
              nFile.pop(nFile.index(i))
  for i in nFile:
      if i.find("malware") != -1:
          nFile.pop(nFile.index(i))         
  return "PC Files:" + ",".join(nFile) if len(nFile) > 0 else  'PC Files: Empty'

