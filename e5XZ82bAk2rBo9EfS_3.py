
def bed_time(*times):
  wakeuplist = []
  for truetimes in times:
    alarmstring = truetimes[0]
    durationstring  = truetimes[1]
    alarmlist = alarmstring.split(":")
    durationlist = durationstring.split(":")
​
    alarmhour = int(alarmlist[0])
    alarmminute = int(alarmlist[1])
    durationhour = int(durationlist[0])
    durationminute = int(durationlist[1])
​
    wakeupminute = alarmminute - durationminute
    wakeuphour = alarmhour - durationhour
​
    if wakeupminute < 0:
        wakeupminute = 60 + wakeupminute
        wakeuphour -= 1
​
    if wakeuphour < 0:
      wakeuphour = 24 + wakeuphour
​
    if wakeupminute < 10:
        wakeupminutestring = "0" + str(wakeupminute)
    else:
      wakeupminutestring = str(wakeupminute)
      
    if wakeuphour < 10:
      wakeuphourstring = "0" + str(wakeuphour)
    else:
      wakeuphourstring = str(wakeuphour)
    
    wakeuphourstring = wakeuphourstring + ":" + wakeupminutestring
    wakeuplist.append(wakeuphourstring)
​
  return wakeuplist

