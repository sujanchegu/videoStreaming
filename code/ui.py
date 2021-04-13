from flask import Flask, render_template, request
from collections import defaultdict
from recommender import *
from user import *

app = Flask(__name__)
from dbase import *

class ConsumerUI:
    def __init__(self):
        self.logged_in = defaultdict(lambda:'garbage')
        self.recommender = Recommender()

    def register(self, name, email, pwd):
        dude = Consumer() # object of consumer, useris and registerDate will be automatically filled
        dude.register(name, email, pwd) # useris and registerDate will be automatically filled
        db.regUser(dude._consumerName, dude._email, dude._userid, dude._password, dude._registerDate)
        self.logged_in[email] = dude
        self.fetch_updates(dude)
        print("Render Buffer : ",self.render_buffer)

    def logout(self,email):
        del self.logged_in[email]
        print("In ConsumerUI > logout : ",self.logged_in)

    def login(self, email):
        # print("email : ",email)
        user_record = db.retrieveUser(email);
        print("User record : ", user_record);
        self.logged_in[email] = Consumer(user_record[0], user_record[1], user_record[2], user_record[3], user_record[4])

        # consumer1 = Consumer()
        # consumer1.register('sriram', 'sriram@gmail.com', 'allahwhoakbar')
        # consumer1.disp()
        # creator1 = Creator('123', consumer1)
        # creator1.disp()
        # video1 = creator1.Create_video('mandalorian', '1', '58:00', 'awesome show' )
        # video2 = creator1.Create_video('GOT', '2', '58:00', 'S8 Sucks' )
        #
        # self.logged_in[email].Create_Playlist('favourites')
        # self.logged_in[email].Add_To_Playlist('favourites', video1)
        # self.logged_in[email].Add_To_Playlist('favourites', video2)
        #
        # self.logged_in[email].Play_All_Playlist('favourites')

        self.fetch_updates(self.logged_in[email])
        print("Render Buffer : ",self.render_buffer)

    def fetch_updates(self, user):
        self.render_buffer = self.recommender.update(user)

cons = ConsumerUI()

@app.route("/")
def home():
    return render_template('home.html');

@app.route("/log_in")
def log_in():

    return render_template('log_in.html');

@app.route("/verify_user", methods = ['GET' , 'POST'])
def verify_user():
    email = request.form['email']
    name = request.form['name']
    pwd = request.form['pwd']

    if(not db.checkUser(email)):
        cons.register(name, email, pwd)
        print("DB : ", db)
        print("db_table : ")
        db.print_table("users")

        return f"<h1 style = 'color : green; font-family : Arial;'> Account created ! </h1> \
        <a href = '/dashboard'> Go to dashboard </a> \
        <script> document.cookie = \"email = {email}\"; \
        console.log(document.cookie) </script> \
        "
    else:
        return '''
        <h1 style = 'color : red; font-family : Arial;'> Account already exists! Try signing in. </h1>
        <a href = '/log_in'> Sign In </a>
        '''
@app.route("/verify_user1", methods = ['GET','POST'])
def verify_user1():
    email = request.form['email']
    pwd = request.form['pwd']

    if(not db.checkUser(email)):
        return '''<h1 style = 'color : red; font-family : Arial;'> Account not found ! </h1>
        <a href = '/'> Sign Up </a>
        '''
    else:
        cons.login(email)
        return f"<h1 style = 'color : green; font-family : Arial;'> Logged in successfully ! </h1> \
        <a href = '/dashboard'> Go to dashboard </a> \
        <script> document.cookie = \"email = {email}\"; \
        console.log(document.cookie) </script> \
        "

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')

@app.route("/logout")
def logout():
    email = request.cookies.get('email')
    cons.logout(email)
    return render_template('home.html')

if(__name__ == '__main__'):
    app.run(debug = True);
