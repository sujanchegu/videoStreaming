from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html');

@app.route("/log_in")
def log_in():
    return render_template('log_in.html');

if (__name__ == '__main__'):
    app.run(debug = True);
