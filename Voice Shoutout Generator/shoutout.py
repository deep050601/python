import win32com.client as wincl

name = ["deep","yug",'manav','shani','kush','rydham','gaurav','hil','harsh','monil','kaival','mundi','ashish','jaydip','modi','dhruv']
speaker = wincl.Dispatch("SAPI.SpVoice")
for i in name:
    speaker.Speak("Shoutout to " + i)
    print("to stop enter -1")
    if input()==-1:
        break