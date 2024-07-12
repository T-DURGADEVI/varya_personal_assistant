import text_to_speech
import speech_to_text
import datetime
import webbrowser
import weather

def Action(data):
    user_data = data.lower()

    if "what is your name" in user_data:
        text_to_speech.text_tospeech("My name is Varya")
        return "My name is Varya"

    elif "hello" in user_data or "hai" in user_data:
        text_to_speech.text_tospeech("hai how i can help you")
        return "hai how i can help you"

    elif "good morning" in user_data:
        text_to_speech.text_tospeech("good morning")
        return "good morning"

    elif "time now" in user_data:
        current_time=datetime.datetime.now()
        time=(str)(current_time)+"hour",(str)(current_time.minute)+"Minute"
        text_to_speech.text_tospeech(time)
        return time

    elif "shutdown" in user_data:
        text_to_speech.text_tospeech("Ok")
        return "Ok"
    
    elif "play music" in user_data:
        webbrowser.open("https://gaana.com/")
        text_to_speech.text_tospeech("gaana.com is now ready for you")
        return "gaana.com is now ready for you"

    elif "open youtube" in user_data:
        webbrowser.open("https://youtube.com/")
        text_to_speech.text_tospeech("youtube.com is now ready for you")
        return "youtube.com is now ready for you"

    elif "open google" in user_data:
        webbrowser.open("https://google.com/")
        text_to_speech.text_tospeech("google.com is now ready for you")
        return "google.com is now ready for you"
    
    elif "weather" in user_data:
        ans= weather.weather_find()
        text_to_speech.text_tospeech(ans)
        return ans

    else:
        text_to_speech.text_tospeech("I'm not able to understand")
        return "I'm not able to understand"

