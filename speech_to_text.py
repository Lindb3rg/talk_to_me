import speech_recognition as sr
import pyttsx3
import os
import openai

from dotenv import load_dotenv
load_dotenv()

OPENAI_KEY = os.getenv("OPENAI_KEY")
openai.api_key = "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"
engine = pyttsx3.init()
# Recognizer
r = sr.Recognizer()

# Speak back
def SpeakText(command, engine):
    try:
        engine.say(command)
        engine.runAndWait()
    except Exception as e:
        print(f"An error occurred: {e}")

def record_text():
    while(1):
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                print("I'm listening")
                audio2 = r.listen(source2)
                my_text = r.recognize_google(audio2,)
                # For Swedish: language='sv-SE'
                return my_text


        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
        
        except sr.UnknownValueError:
            print("Unknown error occured")

    return





def send_to_chatGBT(messages, model="gpt-3.5-turbo"):

    response = openai.ChatCompletion.create(
        model = model,
        messages = messages,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5
    )
    message = response.choices[0].message.content
    messages.append(response.choices[0].message)
    return message

messages = [{"role":"user","content":"Please act like Jarvis from Iron man."}]

while(1):
    text = record_text()
    messages.append({"role":"user","content":text})
    response = send_to_chatGBT(messages)
    SpeakText(response)
    print(response)



def output_text(text):
    f = open("output.txt", "a")
    f.write(text)
    f.write("\n")
    f.close()
    return



