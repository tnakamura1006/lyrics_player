import time
from package.music_player_controller import MusicPlayerControllerInterface
from package.lyrics_output_controller import LyricsOutputControllerInterface
from package.lyrics_data_controller import LyricsDataControllerInterface

class LyricsPlayManager:
  def __init__(
      self,
      MusicPlayerController: MusicPlayerControllerInterface,
      LyricsOutputController: LyricsOutputControllerInterface,
      LyricsDataController: LyricsDataControllerInterface
  ):
    self.MusicPlayerController = MusicPlayerController
    self.LyricsOutputController = LyricsOutputController
    self.LyricsDataController = LyricsDataController

  def exec(self):
    temp_music_info = {}
    while (1):
      play_music_info = self.MusicPlayerController.get_play_music_info()
      if play_music_info and play_music_info['music_player_status'] == 1:
        if temp_music_info != play_music_info:
          temp_music_info = play_music_info
          self.test_output(play_music_info)
      print('loop')
      time.sleep(3)

  def test_output(self, play_music_info):
    print(play_music_info['track_name'])
    print(play_music_info['artist_name'])
    lyric_data = self.LyricsDataController.get_lyric(play_music_info['track_name'], play_music_info['artist_name'])

    if lyric_data != None:
      records = lyric_data['lyrics_records']
      for record in records:
        while 1:
          if self.time_judge(record['second']):
            self.LyricsOutputController.output(record)
            break
          time.sleep(0.75)

  def time_judge(self, second: int):
    if second <= self.MusicPlayerController.get_current_play_time():
      return 1
    return 0
