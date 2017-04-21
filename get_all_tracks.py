from get_flac_tracks import get_artist_and_title
from get_cue_tracks import get_artist_and_title_cue

lib_path = "C:\\Users\\vladm\\Music"
exclude = ["5'nizza", "Alai Oli", "MusicBee", "NoizeMC", "SunSay", "?????? ???????"]

def all_tracks(folder, exclude_folders):
    tracks_part_1 = get_artist_and_title(folder, exclude_folders)
    tracks_part_2 = get_artist_and_title_cue(folder, exclude_folders)
    all_tracks = tracks_part_1.items() + tracks_part_2.items()
    return all_tracks

print all_tracks(lib_path, exclude)
