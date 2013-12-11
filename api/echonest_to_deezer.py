import json
import urllib2

def title_artist_to_deezer_tid(key, title, artist):
#   
# This function returns the Deezer track id matching the couple 
# (track title * artist name) thanks to a http query to the Echonest API
#
# input:
#   - key (string) : development key for the use of the Echonest API
#   - artist (string) : the artist's name for the track
#   - title (string) : the title of the track
# output:
#   - the deezer track id (string)
#
# ex: title_artist_to_deezer_tid("GXGVZDP19FKVQYUBO","karma police","radiohead")
#
    artist = urllib2.quote(artist) # format the artist name to a url-safe string
    title = urllib2.quote(title) # format the title name to a url-safe string
    url = "http://developer.echonest.com/api/v4/song/search?api_key=" + key # add dev key
    url += "&format=json&results=1&artist=" + artist # add artist
    url += "&title=" + title + "&bucket=id:deezer&bucket=tracks&limit=true" # add title and ask for deezer information
    answer = urllib2.urlopen(url).read() # store the answer to the http query
    decoded = json.loads(answer) # translate the json answer
    deezer_id = decoded['response']['songs'][0]['tracks'][0]['foreign_id'] # extract deezer track id
    return deezer_id.split(':').pop()

def title_artist_to_echonest_tid(key, title, artist):
#   
# This function returns the Echonest track id (in the Deezer space) matching 
# the couple (track title * artist name) thanks to a http query to the Echonest API
#
# input:
#   - key (string) : development key for the use of the Echonest API
#   - artist (string) : the artist's name for the track
#   - title (string) : the title of the track
# output:
#   - the echonest track id (string)
#
# ex: title_artist_to_echonest_tid("GXGVZDP19FKVQYUBO","karma police","radiohead")
#
    artist = urllib2.quote(artist) # format the artist name to a url-safe string
    title = urllib2.quote(title) # format the title name to a url-safe string
    url = "http://developer.echonest.com/api/v4/song/search?api_key=" + key # add dev key
    url += "&format=json&results=1&artist=" + artist # add artist
    url += "&title=" + title + "&bucket=id:deezer&bucket=tracks&limit=true" # add title and ask for deezer information
    answer = urllib2.urlopen(url).read() # store the answer to the http query
    decoded = json.loads(answer) # translate the json answer
    echonest_id = decoded['response']['songs'][0]['tracks'][0]['id'] # extract deezer track id
    return echonest_id
    
def echonest_tid_to_deezer_tid(key, tid):
#   
# This function returns the Deezer track id matching the Echonest track id
# thanks to a http query to the Echonest API and the function title_artist_to_deezer_tid
#
# input:
#   - key (string) : development key for the use of the Echonest API
#   - tid (string) : the echonest track id
# dependencies:
#   - title_artist_to_deezer_tid()
# output:
#   - the deezer track id (string)
#
# ex: echonest_tid_to_deezer_tid("GXGVZDP19FKVQYUBO","TRAGHDU139CE0EF708")
#
    url = "http://developer.echonest.com/api/v4/track/profile?api_key=" + key # add dev key
    url += "&format=json&id=" + tid + "&bucket=audio_summary" # add echonest track id
    answer = urllib2.urlopen(url).read() # store the answer to the http query
    decoded = json.loads(answer) # translate the json answer
    artist = decoded['response']['track']['artist']
    title = decoded['response']['track']['title'] 
    return title_artist_to_deezer_tid(key, title, artist)

print echonest_tid_to_deezer_tid("GXGVZDP19FKVQYUBO","TRAGHDU139CE0EF708")
print title_artist_to_deezer_tid("GXGVZDP19FKVQYUBO","karma police","radiohead")
print title_artist_to_echonest_tid("GXGVZDP19FKVQYUBO","karma police","radiohead")