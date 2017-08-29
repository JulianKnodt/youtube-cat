from pytube import YouTube
from pydub import AudioSegment
import csv
from glob import glob
from os import path
import uuid
import sys

unique_names = {}

def convertHhMmSsToMs(hhmmss):
  vals = hhmmss.split(':')
  vals = ['0'] * (3 - len(vals)) + vals
  vals = map(lambda a: 1000 * a, map(float, vals))[::-1]
  accum = vals[0] + vals[1] * 60 + vals[2] * 3600
  return accum

def convertSecToMs(sec): float(sec) * 1000

if len(sys.argv) < 2:
  print("No file argument passed")
  exit()

with open(sys.argv[1]) as csvfile:
  print("starting to process")
  youtube_values = csv.reader(csvfile, delimiter=',', quotechar='"')

  parts = []

  for row in youtube_values:
    if len(row) == 0 or row[0] == 'comment' or row[0] == 'c': continue
    youtube_url = row[-1]

    if youtube_url != '-' and youtube_url not in unique_names:
      yt = YouTube(row[-1])
      video = yt.filter('mp4')[-1]
      mp4_path = './mp4/%s.mp4' % (video.filename)
      if not path.isfile('./mp4/%s.mp4' % (video.filename)):
        sys.stdout.write('.')
        video.download('./mp4')
      start_ms = convertHhMmSsToMs(row[0])
      end_ms = round(start_ms + (float(row[1]) * 1000))
      start_ms = round(start_ms)
      song = AudioSegment.from_file(mp4_path, 'mp4')[start_ms:end_ms]
      parts.append(song)
      sys.stdout.write('.')
    elif youtube_url == '-':
      parts.append(AudioSegment.silent(duration=float(row[0])*1000))

  output = reduce(lambda a, b: a.append(b, crossfade=2000), parts)

  sys.stdout.write('done.\n')
  name = str(uuid.uuid4())[:12]

  out_f = open("./output/%s_mix.mp3" % name, 'wb+')
  output.export(out_f, format='mp3')


# Clean up

# print('-'*73)
# print('-'*30 + '   CLEANING   ' + '-'*30)
# print('-'*73)

# files = glob('./mp3/*')
# for file in files:
  # remove(file)
