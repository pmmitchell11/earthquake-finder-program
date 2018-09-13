# Project 5
#
# Name: Parker Mitchell
# Instructor: Hatalsky
# Section: 11

from math import *
from urllib.request import *
from json import *
from datetime import datetime
import time
from operator import *


def get_json(url):
   ''' Function to get a json dictionary from a website.
       url - a string'''
   with urlopen(url) as response:
      html = response.read()
   htmlstr = html.decode("utf-8")
   return loads(htmlstr)

def time_to_str(time):
   ''' Converts integer seconds since epoch to a string.
       time - an int '''
   return datetime.fromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')    
   

class Earthquake:
   '''A class to represent an Earthquake
      Attributes:
          place - a string
          mag - a float
          longitude - a float
          latitude - a float
          time - an int'''

   def __init__(self, place, mag, longitude, latitude, time):
      self.place = place
      self.mag = mag
      self.longitude = longitude
      self.latitude = latitude
      self.time = time

   def __eq__(self, other):
      return (self.place == other.place and
              isclose(self.mag, other.mag) and
              isclose(self.longitude, other.longitude) and
              isclose(self.latitude, other.latitude) and
              self.time == other.time)

   def __str__(self):
      return ("(%.2f) %40s at %s (%8.3f, %6.3f)" % (self.mag, self.place, time_to_str(self.time), self.longitude, self.latitude))




def read_quakes_from_file(filename):

   # read in a text file and create earthquake objects, then append those new objects to a 'quake' list

   f = open(filename, 'r')
   quakes = []

   for line in f:
      line = line.split()
      mag = float(line[0])
      longitude = float(line[1])
      latitude = float(line[2])
      quake_time = int(line[3])
      place = ' '.join(line[4:])
      quake = Earthquake(place, mag, longitude, latitude, quake_time)
      quakes.append(quake)

   return quakes



def filter_by_mag(quakes, low, high):
   filtered = []

   for quake in quakes:
      if quake.mag >= low and quake.mag <= high:
         filtered.append(quake)

   return filtered


def filter_by_place(quakes, word):
   filtered = []

   for quake in quakes:
      if word.lower() in quake.place.lower() or word.upper() in quake.place.upper():
         filtered.append(quake)

   return filtered


def quake_from_feature(feature):

   place = feature["properties"]["place"]
   mag = feature["properties"]["mag"]
   quake_time = int(feature["properties"]["time"] / 1000)  # converts from ms to s
   longitude = feature["geometry"]["coordinates"][0]
   latitude = feature["geometry"]["coordinates"][1]

   quake = Earthquake(place, mag, longitude, latitude, quake_time)

   return quake


def display_data(quakes):
   print('Earthquakes:')
   print('------------')
   for quake in quakes:
      print(quake)



def print_options():
   print("\nOptions:\n"
         "  (s)ort\n"
         "  (f)ilter\n"
         "  (n)ew quakes\n"
         "  (q)uit\n")

   choice = input('Choice: ')

   return choice


def write_out(quakes):
   out = open('quakes.txt', 'w')  # write or read??

   for quake in quakes:
      mag = str(quake.mag)
      long = str(quake.longitude)
      lat = str(quake.latitude)
      time = str(quake.time)
      place = str(quake.place)

      out.write("%s %s %s %s %s\n" % (mag, long, lat, time, place))




'''questions

-how to go from date to epoch timestamp?
-writing out to a file new line stuff???
-when writing back out, should a magnitude of 2.80 --> 2.8 in the file??

'''