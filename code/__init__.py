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
db.addVideo('20s_Video', '20_SECOND_TIMER_.mp4', "Alarm", 'abc@gmail.com', 0.20,'2014-9-1', 22355, 7995)
db.addVideo('Coca_Cola_Video', 'Coca-Cola_20_Second_Commercial_Video.mp4', "Coke Ad", 'abc@gmail.com', 0.23,'2014-9-1', 22345, 7895)
db.addVideo('Kandima_Video', 'Kandima_Signature_Video_-_20_seconds.mp4', "Maldives Ad", 'abc@gmail.com', 0.20,'2014-9-1', 2345, 795)

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
