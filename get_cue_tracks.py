from get_mlib import get_all_tracks

def get_artist_and_title_cue(path, exclusion):
    artist = ''
    cue_tracks = {}
    tracks = get_all_tracks(path, exclusion)[0]

    for track in tracks.values():
        cue = open(track, 'r')
        lines = cue.readlines()
        try:
            artist = filter(lambda line: line.startswith("PERFORMER"), lines)[0].split('"')[1]
        except IndexError:
            artist = 'Unknown'
        track_list = [song.split('"')[1] for song in filter(lambda line: line.startswith('    TITLE'), lines)]
        for track in track_list:
            cue_tracks[track] = artist

    return cue_tracks
