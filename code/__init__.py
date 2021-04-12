from dbase import *
from video import *
from history import *
from playlist import *
import os

#DBASE

db.regUser('abc', 'abc@gmail.com', 'passwd', '12-12-2012', '456456456456', 0)
print(db.checkUser('def@gmail.com'))
db.regCreator('abc@gmail.com')
print(db.checkUser('abc@gmail.com'))
db.addVideo('sriram eating', 'video1', 'bennur too', 'abc@gmail.com', 23.45, 123, 456)
db.addVideo('shashank eating', 'video2', 'sriram too', 'abc@gmail.com', 23.45, 123, 456)
db.addVideo('bennur eating', 'video3', 'shashank too', 'abc@gmail.com', 23.45, 123, 456)
db.addVideo('sujan eating', 'video4', 'sujan too', 'abc@gmail.com', 23.45, 123, 456)
os.system('touch ../assets/videos/video4.mp4')
db.deleteVideo('video4')
db.incAttr('video1', 'views', 5)

#VIDEO
sampleVideoObject1 = Video('sriram eating', 'video1', 23.45, 'bennur too', 'abc@gmail.com')
sampleVideoObject2 = Video('shashank eating', 'video2', 23.45, 'sriram too', 'abc@gmail.com')
sampleVideoObject3 = Video('bennur eating', 'video3', 23.45, 'shashank too', 'abc@gmail.com')

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

db.addHistory(sampleHistoryObject1)
print(db.retrieveHistory('abc@gmail.com'))

db.addHistory(sampleHistoryObject2)
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