from flask import Flask, request, jsonify
import yt_dlp

app = Flask(__name__)

@app.route('/download', methods=['POST'])
def download_video():
    data = request.json
    url = data.get("video_url")
    if not url:
        return jsonify({"error": "No video_url provided"}), 400

    ydl_opts = {
        'outtmpl': 'videos/%(title)s.%(ext)s',
        'format': 'best[ext=mp4]',
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return jsonify({"status": "Download complete"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
