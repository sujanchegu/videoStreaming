from flask import Flask, render_template
app = Flask(__name__)
from dbase import *

@app.route("/")
def home():
    return render_template('home.html');

@app.route("/log_in")
def log_in():
    return render_template('log_in.html');

if (__name__ == '__main__'):
    app.run(debug = True);

class ConsumerUI:
    def __init__(self):
        self.logged_in = defaultdict(lambda:'garbage')
        self.recommender = Recommeder()

    def register(self, name, email, pwd):
        dude = Consumer() # object of consumer, useris and registerDate will be automatically filled
        dude.register(name, email, pwd) # useris and registerDate will be automatically filled
        db.regUser(dude._consumerName, dude._email, dude._userid, dude._password, dude._registerDate)
        self.logged_in[email] = dude


    def login(self):
        None

    def fetch_updates(self):
        None
