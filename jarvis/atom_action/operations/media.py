import sys

sys.dont_write_bytecode = True
from jarvis.atom_action.src import *

def view_document(file_path) -> None:
    return evince(file_path)

def play_audio(file_path) -> None:
    return rhythmbox_client(f"--play-uri=\"{file_path}\"")

def play_video(file_path) -> None:
    return totem(file_path)


path = "/home/heroding/桌面/CCF.pdf"
view_document(path)