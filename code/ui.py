from flask import Flask, render_template, request
from collections import defaultdict
from recommender import *
from user import *
from topvideos import *
import json

app = Flask(__name__, static_folder = 'static')

from dbase import *
name_ = ""
email_ = ""

class ConsumerUI:
    def __init__(self):
        self.logged_in = defaultdict(lambda:'garbage')
        self.recommender = Recommender()
        self.recommend_buffer = []

    def register(self, name, email, pwd):
        dude = Consumer() # object of consumer, useris and registerDate will be automatically filled
        dude.register(name, email, pwd) # useris and registerDate will be automatically filled
        db.regUser(dude._consumerName, dude._email, dude._userid, dude._password, dude._registerDate)
        self.logged_in[email] = dude
        self.fetch_updates(dude, True)
        # for c in self.recommend_buffer:
        #     c.disp()

    def logout(self,email):
        if(email in self.logged_in):
            del self.logged_in[email]
        self.recommend_buffer.clear()
        print("In ConsumerUI > logout : ",self.logged_in)

    def login(self, email):
        # print("email : ",email)
        user_record = db.retrieveUser(email);
        print("User record : ", user_record);
        self.logged_in[email] = Consumer(user_record[0], user_record[1], user_record[1],user_record[2], user_record[3])

        consumer1 = Consumer()
        consumer1.register('sriram', 'sriram@gmail.com', 'allahwhoakbar')
        consumer1.disp()
        creator1 = Creator('123', consumer1)
        creator1.disp()
        # video1 = creator1.Create_video('mandalorian', '1', '58.00', 'awesome show' )
        # video2 = creator1.Create_video('GOT', '2', '58.00', 'S8 Sucks' )
        #
        # self.logged_in[email].Create_Playlist('favourites')
        # self.logged_in[email].Add_To_Playlist('favourites', video1)
        # self.logged_in[email].Add_To_Playlist('favourites', video2)

        # self.logged_in[email].Play_All_Playlist('favourites')

        self.fetch_updates(self.logged_in[email], False)
        print("Recommend Buffer : \n",self.recommend_buffer)
        print("Mostly Viewed Buffer : \n",self.mostViewed_buffer)
        print("Mostly Like Buffer : \n",self.mostLiked_buffer)
        print("Recently Uploaded Buffer : \n",self.recentlyUpload_buffer)
        print("Recent History : \n", self.recent_history)
        print("Favourites : \n", self.favourites)
        print("Liked : \n", self.liked)
        
        # print("Loop in login : ")
        # for c in self.recommend_buffer:
        #     c.disp()

    def fetch_updates(self, user, reg_flag):
        if(not reg_flag):
            self.recommend_buffer = self.recommender.update(user)
        topVideos = obj.getTopVideos()
        self.mostViewed_buffer, self.mostLiked_buffer, self.recentlyUpload_buffer = topVideos[0], topVideos[1], topVideos[2]

        self.recent_history = db.retrieveHistory(user._email)[0]
        self.favourites = db.retrievePlaylist(user._email, 'favourites')
        self.liked = db.retrievePlaylist(user._email, 'liked')


cons = ConsumerUI()

@app.route("/")
def home():
    return render_template('home.html');

@app.route("/log_in")
def log_in():

    return render_template('log_in.html');

@app.route("/verify_user", methods = ['GET' , 'POST'])
def verify_user():
    global name_;
    global email_;
    email = request.form['email']
    name = request.form['name']
    pwd = request.form['pwd']
    name_ = name;
    email_ = email;

    if(not db.checkUser(email)):
        cons.register(name, email, pwd)
        print("DB : ", db)
        print("db_table : ")
        db.print_table("users")

        return f"<h1 style = 'color : green; font-family : Arial;'> Account created ! </h1> \
        <a href = '/dashboard'> Go to dashboard </a> \
        "
    else:
        return '''
        <h1 style = 'color : red; font-family : Arial;'> Account already exists! Try signing in. </h1>
        <a href = '/log_in'> Sign In </a>
        '''
@app.route("/verify_user1", methods = ['GET','POST'])
def verify_user1():
    global name_;
    global email_;
    email = request.form['email']
    pwd = request.form['pwd']
    name_ = db.retrieveUser(email)[0]
    email_ = email;

    if(not db.checkUser(email)):
        return '''<h1 style = 'color : red; font-family : Arial;'> Account not found ! </h1>
        <a href = '/'> Sign Up </a>
        '''
    else:
        cons.login(email)
        return f"<h1 style = 'color : green; font-family : Arial;'> Logged in successfully ! </h1> \
        <a href = '/dashboard'> Go to dashboard </a> \
        "

@app.route("/dashboard")
def dashboard():
    global name_;
    global email_;
    return render_template('dashboard.html', name1 = name_, email1 = email_, rec = json.dumps(list(cons.recommend_buffer)), mv = json.dumps(list(cons.mostViewed_buffer)), ml = json.dumps(list(cons.mostLiked_buffer)), ru = json.dumps(list(cons.recentlyUpload_buffer)))

@app.route("/dashboard/manage_prof")
def dashboard_mp():
    return '''
    <h1> Manage Profile </h1>
    <a href="/dashboard">Go back</a>
    '''

@app.route("/logout")
def logout():
    global email_;
    cons.logout(email_)
    return render_template('home.html')

@app.route("/updateStats", methods = ['POST'])
def updateStats():

    print("Here in update stats")

    global email_;
    for key in request.form:
        uri = key[0:-6]
        attr = key[-5:]
        print("\n\nupdateStats > uri : ", uri,"\n\nupdateStats > attr : ", attr);
        vid_info = db.retrieveParticularVideo(uri)
        if(attr == "playl"):
            print("\n\nAdding to playlist...\n\n")
            db.addToPlaylist(Playlist("favourites", email_), Video(vid_info[0],vid_info[1],vid_info[-2],vid_info[2],vid_info[-3],vid_info[3],vid_info[4]))
        else:
            db.incAttr(uri, attr, int(request.form[key]))
            if(attr == "views"):
                db.addVideoToHistory(Video(vid_info[0],vid_info[1],vid_info[-2],vid_info[2],vid_info[-3],vid_info[3],vid_info[4]), email_)
                print(db.retrieveHistory(email_))
            else:
                db.addToPlaylist(Playlist("liked", email_), Video(vid_info[0],vid_info[1],vid_info[-2],vid_info[2],vid_info[-3],vid_info[3],vid_info[4]))
    return ""

if __name__ == '__main__':
  app.run(host='127.0.0.1', port = 5000, debug = True)
