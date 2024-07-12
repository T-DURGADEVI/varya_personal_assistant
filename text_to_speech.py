import pyttsx3

def text_tospeech(text):
    engine = pyttsx3.init()

    # Set the speaking rate (optional)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 70)

    # Set the specific voice by ID
    voice_id = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0'
    engine.setProperty('voice', voice_id)

    # Speak the text
    engine.say(text)
    engine.runAndWait()



