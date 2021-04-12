from flask import Flask, render_template, request
import secrets

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '../assets/videos/'

@app.route('/upload')
def upload_video():
    return render_template('upload.html')

@app.route('/uploader', methods = ['POST'])
def upload_video():
    f = request.files['file']
    vid_uri = secrets.token_hex(nbytes=16)
    
    #TODO add the video to the videoDB

    f.save(vid_uri + '.mp4')
    

if __name__ == '__main__':
    app.run(debug = True)