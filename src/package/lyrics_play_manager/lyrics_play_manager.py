import time
from package.music_player_controller import *
from package.lyrics_output import *

class LyricsPlayManager:
  def __init__(self, musicPlayerController: MusicPlayerControllerInterface, lyricsOutput: LyricsOutputInterface):
    self.musicPlayerController = musicPlayerController
    self.lyricsOutput = lyricsOutput

  def exec(self):
    while (1):
      play_music_info = self.musicPlayerController.get_play_music_info()
      if play_music_info and play_music_info['player_state'] == 1:
        self.lyricsOutput.output(play_music_info)
        break
      print('loop')
      time.sleep(1)
