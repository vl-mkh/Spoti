import os

def get_all_tracks(path, exclusion):

    lib_flac = {}
    lib_cue = {}

    for root, dirs, files in os.walk(path, topdown=True):
        dirs[:] = list(filter(lambda x: not x in exclusion, dirs))
        for file in files:
            try:
                if file.split('.')[1] in ('cue', 'flac', 'm4a', 'mp3'):
                    lib_flac[file] = os.path.join(root, file)
            except IndexError:
                pass


    for key in lib_flac.keys():
        if key.endswith('cue'):
            lib_cue[key] = lib_flac.pop(key)


    for key_flac in lib_flac.keys():
        if (key_flac.split('.')[0] + '.cue') in lib_cue.keys():
             del lib_flac[key_flac]


    return [lib_cue, lib_flac]
