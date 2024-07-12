import speech_recognition as sr

def speech_to_text1():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)
        try:
            voice_data=""
            voice_data=r.recognize_google(audio)
            return voice_data
        except sr.UnknownValueError:
            print("error")
        except sr.RequestError:
            print("RequestError")



# import speech_recognition as sr
# from pydub import AudioSegment
# from pydub.effects import normalize, low_pass_filter
# import os

# def preprocess_audio(audio_data):
#     # Save raw audio to a temporary file
#     raw_audio_file = "raw_audio.wav"
#     with open(raw_audio_file, "wb") as f:
#         f.write(audio_data.get_wav_data())

#     # Load and preprocess the audio
#     audio = AudioSegment.from_file(raw_audio_file)
#     audio = normalize(audio)
#     audio = low_pass_filter(audio, cutoff=3000)

#     # Save the processed audio to a new file
#     processed_audio_file = "processed_audio.wav"
#     audio.export(processed_audio_file, format="wav")
#     os.remove(raw_audio_file)  # Clean up the raw audio file
#     return processed_audio_file

# # Create a recognizer object
# r = sr.Recognizer()

# # Use the microphone as the audio source
# try:
#     with sr.Microphone() as source:
#         print("Adjusting for ambient noise, please wait...")
#         r.adjust_for_ambient_noise(source, duration=1)  # Adjusts for ambient noise
#         print("Please say something")
#         audio = r.listen(source)
#         print("Got it! Now recognizing...")

#         # Preprocess the audio
#         processed_audio_file = preprocess_audio(audio)

#         # Recognize speech using Google Speech Recognition on the processed audio
#         with sr.AudioFile(processed_audio_file) as source:
#             processed_audio = r.record(source)
#             try:
#                 voice_data = r.recognize_google(processed_audio)
#                 print("You said: " + voice_data)
#             except sr.UnknownValueError:
#                 print("Google Speech Recognition could not understand audio")
#             except sr.RequestError as e:
#                 print("Could not request results from Google Speech Recognition service; {0}".format(e))
#         os.remove(processed_audio_file)  # Clean up the processed audio file
# except Exception as e:
#     print("Error: {0}".format(e))



