from st_audiorec import st_audiorec
import streamlit as st
import openai
import os
wav_audio_data = st_audiorec()


from dotenv import load_dotenv, dotenv_values
load_dotenv()

client = openai.OpenAI(api_key= os.getenv('OPENAI_API_KEY'))
if wav_audio_data is not None:
    st.audio(wav_audio_data, format='audio/wav')
    print(type(wav_audio_data))
    with open('myfile.wav', mode='bw') as f:
        f.write(wav_audio_data)
    audio_file= open("myfile.wav", "rb")
    transcript = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file
    )
    print(transcript.text)
