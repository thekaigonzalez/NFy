# Written by Kai Gonzalez (C) All rights reserved.

# All software that are sub-software of the NFy audio service follow the same spec as the NFy main project.

import subprocess
import ffmpeg
import argparse

parser = argparse.ArgumentParser("mp3toogg")

parser.add_argument("FILE", help="File to transfer from MP3")

args = parser.parse_args()

subprocess.run(['ffmpeg', '-i', args.FILE, args.FILE[:args.FILE.find(".")] + ".ogg"])