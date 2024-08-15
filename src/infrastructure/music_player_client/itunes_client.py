import win32com.client

class ItunesClient:
  def __init__(self):
    # iTunes COMオブジェクトに接続
    self.iTunes = win32com.client.Dispatch("iTunes.Application")

  def get_play_music_info(self):

    # 現在再生中の曲を取得
    current_track = self.iTunes.CurrentTrack
    # プレイヤーの状態を取得
    player_state = self.iTunes.PlayerState

    music_info = {}
    if current_track:
        # 曲の情報を取得
        music_info = {
          'track_name' : current_track.Name,
          'artist_name' : current_track.Artist,
          'album_name' : current_track.Album,
          'player_state' : player_state,  # 0:停止中/ 1:再生中
        }
    return music_info
