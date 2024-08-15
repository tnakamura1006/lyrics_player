import time
from package.music_player_controller import *
from infrastructure.music_player_client.itunes_client import *
from package.lyrics_output_controller import *
from infrastructure.lyrics_output.console_output import *

class LyricsPlayManager:
  def __init__(self):
    self.MusicPlayerController = MusicPlayerController(ItunesClient())
    self.LyricsOutputController = LyricsOutputController(ConsoleOutput())

  def exec(self):
    while (1):
      play_music_info = self.MusicPlayerController.get_play_music_info()
      if play_music_info and play_music_info['player_state'] == 1:
        self.LyricsOutputController.output(play_music_info)
        break
      print('loop')
      time.sleep(1)
