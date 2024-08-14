import sys
sys.path.append('../')
from music_player_controller import ItunesController
from lyrics_output import LyricsConsoleOutput
from lyrics_play_manager import *

if __name__ == "__main__":
  LyricsPlayManager = LyricsPlayManager(ItunesController(), LyricsConsoleOutput())
  LyricsPlayManager.exec()
