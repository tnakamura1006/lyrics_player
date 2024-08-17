import win32com.client
from .music_player_client_interface import MusicPlayerClientInterface

class ItunesClient(MusicPlayerClientInterface):
  def __init__(self):
    # iTunes COMオブジェクトに接続
    self.iTunes = win32com.client.Dispatch("iTunes.Application")

  def get_current_track(self):
    current_track = self.iTunes.CurrentTrack
    return {} if current_track == None else {
      'track_name' : current_track.Name,
      'artist_name' : current_track.Artist,
      'album_name' : current_track.Album,
      'total_time' : current_track.Duration
    }

  def get_music_player_status(self):
    player_state = self.iTunes.PlayerState  # 0:停止中/ 1:再生中
    return {
      'music_player_status' : player_state
    }

  def get_current_play_time(self):
    current_play_time = self.iTunes.PlayerPosition
    return {
      'current_play_time' : current_play_time
    }
