from package.music_player_controller import ItunesController
from package.lyrics_output import LyricsConsoleOutput
from package.lyrics_play_manager import *

if __name__ == "__main__":
  LyricsPlayManager = LyricsPlayManager(ItunesController(), LyricsConsoleOutput())
  LyricsPlayManager.exec()
