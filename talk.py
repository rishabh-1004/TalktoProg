from gtts import gTTS
import os
import speech_recognition as sr
import time

def gtts(word):
	txt=gTTS(text=word,lang='en')
	txt.save("gtts.mp3")
	print("Speaking: "+ word + ".")
	os.system("mpg123 gtts.mp3")
	print("")

def rec():
	print("Listening..")
	r=sr.Recognizer()
	with sr.Microphone() as source:
		audio=r.listen(source)
	print("Processing..")
	print("")
	try:
		text=r.recognize_google(audio)
		print("You said: "+text)
	except Exception as error:
		print(error)
	return(text)

def Main():
	system_status=True
	while system_status:
		text=rec()
		time.sleep(3)
		if (text == "quit"):
			 system_status = False
		else:
			gtts(text)
			gtts("Tell me something more.")

if __name__=='__main__':
	Main()
