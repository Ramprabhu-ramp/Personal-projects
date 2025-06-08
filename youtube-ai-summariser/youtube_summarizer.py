from yt_dlp import YoutubeDL
import openai
import os

def download_audio(youtube_url):
    output_file = "audio.%(ext)s"
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'audio.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'noplaylist': True,
        'force_overwrites': True,
        'quiet': True
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])
    return "audio.mp3"

def transcribe_audio(file_path):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    with open(file_path, "rb") as audio_file:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
    return transcript["text"]

def summarise_transcript(text):
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You summarise YouTube video transcripts."},
            {"role": "user", "content": f"Summarise this transcript:\n\n{text}"}
        ]
    )
    return response['choices'][0]['message']['content']