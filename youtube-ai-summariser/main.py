from flask import Flask, request, render_template
from youtube_summarizer import download_audio, transcribe_audio, summarise_transcript
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    summary = ""
    if request.method == "POST":
        url = request.form["youtube_url"]
        try:
            audio_file = download_audio(url)
            transcript = transcribe_audio(audio_file)
            summary = summarise_transcript(transcript)
        except Exception as e:
            summary = f"Error: {str(e)}"
    return render_template("index.html", summary=summary)

if __name__ == "__main__":
    app.run()