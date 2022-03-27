# Written by Kai Gonzalez (C) All rights reserved.

# All software that are sub-software of the NFy audio service follow the same spec as the NFy main project.

from glob import glob
import pathlib
import subprocess
import ffmpeg
import argparse

parser = argparse.ArgumentParser("mp3toogg")

args = parser.parse_args()

if pathlib.Path("songs_compile").exists():
    for m in glob("songs_compile/*.mp3"):
        subprocess.run(['ffmpeg', '-i', m, m[:m.find(".")] + ".ogg"])