# YouTube AI Summariser

A web-based tool that takes a YouTube video URL and generates a concise summary using automatic transcription (via Whisper) and language generation (via OpenAI GPT models).

⸻

# 🚀 Features
	•	Accepts any valid YouTube URL
	•	Extracts audio using yt-dlp
	•	Transcribes speech to text using OpenAI Whisper
	•	Summarizes content using OpenAI GPT
	•	Web interface built with Flask
	•	Deployable on Google Cloud App Engine

⸻

# 📁 Project Structure

<pre>

youtube-ai-summariser/
├── main.py                  # Entry point for Flask app
├── youtube_summarizer.py   # Core logic for downloading, transcribing, and summarizing
├── app.yaml                # GCP App Engine config
├── requirements.txt        # Python dependencies
├── .env.example            # Template for OpenAI API key
├── templates/
│   └── index.html          # HTML template for the UI
  
</pre>

⸻

# 🧠 How It Works  

1. User submits a YouTube URL  
2. yt-dlp downloads the audio  
3. Whisper model transcribes it to text  
4. GPT model generates a summary  
5. The summary is displayed in the web UI

⸻

# 🛠️ Tech Stack

	•	Python 3.10+
	•	Flask
	•	yt-dlp
	•	OpenAI Whisper
	•	OpenAI GPT API
	•	Google Cloud App Engine

⸻

# 🔒 Environment Setup

Required .env file:

OPENAI_API_KEY=your-openai-key

👉 Never commit your actual .env — use .env.example as a guide.

Install dependencies:

pip install -r requirements.txt


⸻

# 🧪 Local Testing

python main.py

Then open: http://127.0.0.1:5000

⸻

# ☁️ Deployment (GCP App Engine)

Make sure your app.yaml is ready. Then:

gcloud app deploy

App will be hosted at: https://<your-project-id>.appspot.com

⸻

📄 License

MIT License

⸻

🙋‍♂️ Author

Ramprabhu Ravichandran

(Feel free to star, fork, or contribute!)
