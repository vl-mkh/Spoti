from tinytag import TinyTag
from get_mlib import get_all_tracks

def get_artist_and_title(path, exclusion):
    tracks = get_all_tracks(path, exclusion)[1]
    tags = []
    flac_tracks = {}
    map(lambda track: tags.append(TinyTag.get(track)), tracks.values())
    for track in tags:
        flac_tracks[track.title.encode('utf8')] = track.artist.encode('utf8')

    return flac_tracks
