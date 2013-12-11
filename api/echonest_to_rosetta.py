import json
import urllib2

def title_artist_to_rosetta_echonest_tid(key, title, artist, rosetta):
    artist = urllib2.quote(artist) # format the artist name to a url-safe string
    title = urllib2.quote(title) # format the title name to a url-safe string
    url = "http://developer.echonest.com/api/v4/song/search?api_key=" + key # add dev key
    url += "&format=json&artist=" + artist # add artist
    url += "&title=" + title # add title
    url += "&bucket=id:" + rosetta # add the rosetta space id
    url += "&bucket=tracks&limit=true" # limit the result to the rosetta space
    answer = urllib2.urlopen(url).read() # store the answer to the http query
    decoded = json.loads(answer) # translate the json answer
    return decoded['response']['songs']
    
def echonest_tid_to_rosetta_tid(key, tid, rosetta):
    url = "http://developer.echonest.com/api/v4/track/profile?api_key=" + key # add dev key
    url += "&format=json&id=" + tid # add echonest track id
    answer = urllib2.urlopen(url).read() # store the answer to the http query
    decoded = json.loads(answer) # translate the json answer
    artist = decoded['response']['track']['artist'] # get the artist
    title = decoded['response']['track']['title'] # get the title
    songs = title_artist_to_rosetta_echonest_tid(key, title, artist, rosetta) # ask for all possible songs for the couple
    rosetta_tid = "not found"    
    for song in songs:
        for track in song['tracks']:
            if track['id'] == tid:
                rosetta_tid = track['foreign_id'] 
                break
    return rosetta_tid

print echonest_tid_to_rosetta_tid("GXGVZDP19FKVQYUBO", "TRAGHDU139CE0EF708", "deezer")
print echonest_tid_to_rosetta_tid("GXGVZDP19FKVQYUBO", "TRAGHDU139CE0EF708", "musicbrainz")
print echonest_tid_to_rosetta_tid("GXGVZDP19FKVQYUBO", "TRAGHDU139CE0EF708", "spotify-WW")
print echonest_tid_to_rosetta_tid("GXGVZDP19FKVQYUBO", "TRPMTDS139C96EF2B9", "spotify-WW")

#http://developer.echonest.com/api/v4/song/search?api_key=GXGVZDP19FKVQYUBO&format=json&results=2&artist=radiohead&title=karma%20police&bucket=id:deezer&bucket=tracks&limit=true