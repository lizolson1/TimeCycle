import pytube
import os
import sys
from fractions import Fraction



manifest = '/home/drop/lizolson/TimeCycle/DATA/manifest.txt'
youtube_links = '/home/drop/lizolson/TimeCycle/DATA/meta/youtube_links.txt'
datapath = '/home/drop/lizolson/TimeCycle/DATA/vlog/'
mani = open(manifest, "r").readlines()
yt = open(youtube_links, "r").readlines()

for i in range(int(sys.argv[1])):
    link = yt[i].split()
    url = link[0]
    sf = int(link[1])
    ef = int(link[2])
    os.system('youtube-dl ' + url + ' -A')
    title = sorted(os.listdir('.'))[1]
    fps_str = os.popen('ffprobe -v 0 -of csv=p=0 -select_streams v:0 -show_entries stream=r_frame_rate ' + title).read()[:-1]
    #fps = int(Fraction(fps_str))
    fps = float(Fraction(fps_str))
    st = sf / fps
    dur = ef - sf
    #print(sf, dur)
    #print('---- FRAME RATE: ' + str(fps) + '  Start Frame, End Frame   ' + str(sf), str(ef))
    os.system('ffmpeg -ss '+ str(st) +' -i ' + title + ' -c:v libx264 -c:a aac -frames:v ' + str(dur) + ' out' + str(i) + '.mp4')
    #print(mani[i])
    outname = datapath + mani[i][:-1]
    if os.path.isdir(outname) is False:
       os.makedirs(outname, 0o755)
       
    #print('mv ' + 'out' + str(i) + '.mp4 ' + datapath + mani[i][:-1] + 'clip.mp4')
    os.system('mv ' + 'out' + str(i) + '.mp4 ' + datapath + mani[i][:-1] + 'clip.mp4')
    #print(mani[i][:-1])    




