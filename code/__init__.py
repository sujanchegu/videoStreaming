from dbase import *
from video import *
from history import *
from playlist import *
import os


#DBASE

db.regUser('abc', 'abc@gmail.com', 'passwd', '12-12-2012', '456456456456', 0)
db.regUser('xyz', 'xyz@gmail.com', 'passwd', '12-12-2012', '456456456456', 0)
print(db.checkUser('def@gmail.com'))
db.regCreator('abc@gmail.com')
print(db.checkUser('abc@gmail.com'))


db.addVideo('Galaxy S20', 'video1', 'bennur too', 'abc@gmail.com', 13.45,'2012-12-1', 123, 876)
db.addVideo('iPhone12', 'video2', 'sriram too', 'abc@gmail.com', 23.45,'2012-12-2', 98, 97)
db.addVideo('POCO', 'video3', 'shashank too', 'abc@gmail.com', 33.45,'2012-11-1', 657, 123)
# db.addVideo('sujan1', 'video5', 'sujan too', 'abc@gmail.com', 23.45,'2012-10-1', 23, 4566)
# db.addVideo('sujan2', 'video6', 'sujan too', 'abc@gmail.com', 23.45,'2012-9-1', 345, 3344)
# db.addVideo('sujan3', 'video7', 'sujan too', 'abc@gmail.com', 23.45,'2012-9-2', 567, 7885)
# db.addVideo('sujan4', 'video8', 'sujan too', 'abc@gmail.com', 23.45,'2012-8-3', 323, 234)
# db.addVideo('sujan5', 'video9', 'sujan too', 'abc@gmail.com', 23.45,'2013-4-1', 67, 789)
# db.addVideo('sujan6', 'video10', 'sujan too', 'abc@gmail.com', 23.45,'2013-12-1', 22344, 211)
# db.addVideo('sujan7', 'video11', 'sujan too', 'abc@gmail.com', 23.45,'2014-9-1', 99, 456)
db.addVideo('20s_Video', '20_SECOND_TIMER_.mp4', "Alarm", 'abc@gmail.com', 0.37,'2014-9-1', 22355, 7995)
db.addVideo('Coca_Cola_Video', 'Coca-Cola_20_Second_Commercial_Video.mp4', "Coke Ad", 'abc@gmail.com', 0.23,'2014-9-1', 22345, 7895)
db.addVideo('Kandima_Video', 'Kandima_Signature_Video_-_20_seconds.mp4', "Maldives Ad", 'abc@gmail.com', 0.20,'2014-9-1', 2345, 795)
db.addVideo('Desh Ka Rakshak', 'Desh Ka Rakshak Ad (Hindi- 45 Sec).mp4', "Advertisement", 'abc@gmail.com', 0.51,'2014-9-1', 234, 7634)

db.addVideo('Ad', '30 Second TV Ad_ .mp4', "Advertisement", 'abc@gmail.com', 0.32,'2014-9-1', 642, 12445)
db.addVideo('5 Star', '5 Star Ad | 45 Sec (Bengali).mp4', "Advertisement", 'abc@gmail.com', 0.50,'2014-9-1', 1224, 567)
db.addVideo('Climate Change ', 'Climate Change TV Advert - 30 Second.mp4', "Advertisement", 'abc@gmail.com', 0.30,'2014-9-1', 13345, 5467)

db.addVideo('Great for the good', 'Great for the good | ft. Rahul Dravid | CRED.mp4', "Advertisement", 'abc@gmail.com', 0.23,'2014-9-1', 13, 3266)
db.addVideo('Jockey Sport Performance', 'Jockey Sport Performance - Latest TV Ad 30 Sec.mp4', "Advertisement", 'abc@gmail.com', 0.30,'2014-9-1', 131, 5767)
db.addVideo('KIT KAT Celebrates MyBreak', 'KIT KAT Celebrates MyBreak | The Announcer Break 45 Sec | New Ad 2016 | TVC.mp4', "Advertisement", 'abc@gmail.com', 0.47,'2014-9-1', 12445, 674)
db.addVideo('NIKE ', 'NIKE 30 SECONDS AD _ SCHOOL PROJECT.mp4', "Advertisement", 'abc@gmail.com', 0.30,'2014-9-1', 567, 7785)
db.addVideo('NSCC Strive', 'NSCC Strive - 30 sec TV Commercial (Spring 2016).mp4', "Advertisement", 'abc@gmail.com', 0.30,'2014-9-1', 456, 9776)
db.addVideo('The new iPhone SE', 'The new iPhone SE — Apple.mp4', "Advertisement", 'abc@gmail.com', 0.58,'2014-9-1', 4456, 23434)
db.addVideo('BullRingUSA ', 'yt1s.com - 20 Second BullRingUSA Commercial_480p.mp4', "Advertisement", 'abc@gmail.com', 0.21,'2014-9-1', 755, 34565)
db.addVideo('Water', 'yt1s.com - 30 Sec Water Commercial.mp4', "Advertisement", 'abc@gmail.com', 0.30,'2014-9-1', 7886, 345)
db.addVideo('Audi', 'yt1s.com - 30 second Audi commercial.mp4', "Advertisement", 'abc@gmail.com', 0.35,'2014-9-1', 866, 976)
db.addVideo('Ember ', 'yt1s.com - Ember 15 second commercial.mp4', "Advertisement", 'abc@gmail.com', 0.15,'2014-9-1', 754, 8909)
db.addVideo('Ferris State University 2019', 'yt1s.com - Ferris State University 2019 Commercial 30Second Spot  Ferris Forward.mp4', "Advertisement", 'abc@gmail.com', 0.30,'2014-9-1', 3456, 678)
db.addVideo('Hands', 'yt1s.com - Hands  30 Second Ad.mp4', "Advertisement", 'abc@gmail.com', 0.30,'2014-9-1', 234, 6544)
db.addVideo('Pizza aaye', 'yt1s.com - Pizza aaye Free  New Mobile Ordering ad featuring Paresh Rawal.mp4', "Advertisement", 'abc@gmail.com', 0.36,'2014-9-1', 987, 643)

sampleVideoObject1 = Video('Galaxy S20', 'video1', 13.45, 'bennur too', 'abc@gmail.com')
sampleVideoObject2 = Video('iPhone12', 'video2', 23.45, 'sriram too', 'abc@gmail.com')
sampleVideoObject3 = Video('POCO', 'video3', 33.45, 'shashank too', 'abc@gmail.com')

#HISTORY
sampleHistoryObject1 = History('abc@gmail.com')
sampleHistoryObject1.add(sampleVideoObject1)
sampleHistoryObject1.add(sampleVideoObject1)
sampleHistoryObject1.add(sampleVideoObject1)
sampleHistoryObject1.add(sampleVideoObject2)
sampleHistoryObject1.add(sampleVideoObject2)
sampleHistoryObject1.add(sampleVideoObject3)

sampleHistoryObject2 = History('abc@gmail.com')
sampleHistoryObject2.add(sampleVideoObject2)
sampleHistoryObject2.add(sampleVideoObject3)

# db.addHistory(sampleHistoryObject1)
print(db.retrieveHistory('abc@gmail.com'))

# db.addHistory(sampleHistoryObject2)
print(db.retrieveHistory('abc@gmail.com'))

#PLAYLIST
samplePlaylist = Playlist('my-playlist', 'abc@gmail.com')
samplePlaylist.Add_To(sampleVideoObject1)
samplePlaylist.Add_To(sampleVideoObject2)
samplePlaylist.Remove_From(sampleVideoObject2)

#DBASE AGAIN!!!
print('\n'*5)
db.print_table('videos')
print("\n")
db.print_table('users')
print("\n")
db.print_table('[abc@gmail.com]')
print("\n")
db.print_table('[abc@gmail.commy-playlist]')
print("\n")

print("\n\nabc's hist : ",db.retrieveHistory("abc@gmail.com"), "\n\n")
