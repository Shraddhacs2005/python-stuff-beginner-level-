from gtts import gTTS
import os
mytext = 'hello there'
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow = False)
myobj.save("t.mp3")
os.system("t.mp3")
