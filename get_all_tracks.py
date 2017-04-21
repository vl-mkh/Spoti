from get_flac_tracks import get_artist_and_title
from get_cue_tracks import get_artist_and_title_cue

lib_path = "C:\\Users\\vladm\\Music"
exclude = ["5'nizza", "Alai Oli", "MusicBee", "NoizeMC", "SunSay", "?????? ???????"]

tracks_part_1 = get_artist_and_title(lib_path, exclude)
tracks_part_2 = get_artist_and_title_cue(lib_path, exclude)
all_tracks = tracks_part_1.items() + tracks_part_2.items()

print all_tracks
print len(all_tracks)
