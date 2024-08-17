import time
from package.music_player_controller import MusicPlayerControllerInterface
from package.lyrics_output_controller import LyricsOutputControllerInterface

class LyricsPlayManager:
  def __init__(self, MusicPlayerController: MusicPlayerControllerInterface, LyricsOutputController: LyricsOutputControllerInterface):
    self.MusicPlayerController = MusicPlayerController
    self.LyricsOutputController = LyricsOutputController

  def exec(self):
    while (1):
      play_music_info = self.MusicPlayerController.get_play_music_info()
      if play_music_info and play_music_info['player_state'] == 1:
        self.LyricsOutputController.output(play_music_info)
        break
      print('loop')
      time.sleep(1)
