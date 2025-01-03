import speech_recognition as sr
import re
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
def remove_stopwords(text):
    return ' '.join([word for word in text.split() if word not in stop_words])

def clean_text(text):
   
    text = text.lower()


    
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\d+', '', text)

    return text
recognize=sr.Recognizer()
path=r"C:\Users\Asus\Desktop\sample_voice\harvard.wav"

with sr.AudioFile(path) as source:
    print("Loading audio file...")
    audio_data = recognize.record(source)

print("Transcribing audio...")
text= recognize.recognize_google(audio_data)
print(text) # raw text

cleaned_text_1=clean_text(text)
cleaned_text_2=remove_stopwords(text)
print(cleaned_text_2)

