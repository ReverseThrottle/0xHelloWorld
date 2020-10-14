  GNU nano 4.8                                                                                    Project_3.1                                                                                              
#!/usr/bin/python3

# You will need to install lyricsgenius
# pip3 install lyricsgenius
####################################
#                                  #
#       Zachary Hopping            #
#        Project_3.1               #
# Printing Song lyrics to screen   #
#                                  #
####################################

#import lyricsGenius
import lyricsgenius as genius

# Genius API Key
api = genius.Genius("tO7BTSOBtroPd76kJZj6z5gaD9y57vIBZ0bfeIEfApPZzBUdwFeEbq2hrfcRVZqf")

#Search Tame Impala on Genius.com
artist = api.search_artist('Tame Impala', max_songs=3)

#Searches for song Lost in Yesterday
song = api.search_song("Lost In Yesterday", artist.name)

#Prints to screen
print(song.lyrics)
