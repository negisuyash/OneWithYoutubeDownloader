from pytube import YouTube
from flask import Flask, request, send_file, render_template
import json

app = Flask(__name__)
config = json.loads(open('./config.json').read())

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/',methods=['POST'])
def download():
    try:
        return send_file(YouTube(request.form['link']).streams.first().download(),as_attachment=True)
    except Exception:
        return "<script>alert('Somthing went wrong, please check the URL again or it could server memory issue');</script>"


if __name__=='__main__':
    app.run(debug=config['debug'])
