'''
Script : openmw_mod_address_extractor.py
Author : Julien Cabana
Version : 1.0
Date : 2025-12-05
Description : This simple script extracts the paths and file names of an OpenMW mod directory. 
              You then take the data from the output files and copy paste them in openmw.cfg,
              This saves you time from copy-pasting dozens of mods manually.
'''

__author__ = "Julien Cabana"
__version__ = "1.0"
__date__ = "2025-12-05"


from pathlib import Path

root = Path("C:\\OpenMW_mods\\custom\\umo")
destination = Path.cwd()

# Find the path
with open(destination / "mod_paths.txt", "w") as f:

    print("Extracting paths...")
    for dir in root.iterdir():
        path = dir.absolute()
        data_path = "data=\"" + str(path) + "\"\n" 
        f.write(data_path)

# Find the file
with open(destination / "mod_names.txt", "w") as f2:

    valid_ext = {".esp", ".esm", ".omwaddon", ".omwscripts"}

    print("Extracting file names...")
    for file in root.rglob("*"):
        if file.is_file() and file.suffix.lower() in valid_ext:
          file_name = "content=" + str(file) + "\n"
          f2.write(file_name)

#
# Personal Notes
#
# Wrong approach, no need for globs, pathlib already has a way to check for extensions
'''
    # Find mod esp/esm
mod_iter = root.rglob("*.es[m|p]", case_sensitive=False, recurse_symlinks=False)
for mod in mod_iter:
    print(str(mod))
'''
'''    # Find mod omwscripts/omwaddon
mod_iter2 = root.rglob("*.omw*", case_sensitive=False, recurse_symlinks=False)
for mod2 in mod_iter2:
    print(str(mod2))
'''