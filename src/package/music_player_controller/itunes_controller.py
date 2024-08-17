import sys
sys.path.append('../../')
from infrastructure.music_player_client.music_player_client_interface import MusicPlayerClientInterface
from .music_player_controller_interface import MusicPlayerControllerInterface

class ItunesController(MusicPlayerControllerInterface):
  def __init__(self, MusicPlayerClient: MusicPlayerClientInterface):
    self.music_player_client = MusicPlayerClient

  def get_play_music_info(self):
    play_music_info = {}
    current_track = self.music_player_client.get_current_track()
    music_player_status = self.music_player_client.get_music_player_status()
    play_music_info.update(current_track)
    play_music_info['music_player_status'] = music_player_status['music_player_status']
    return play_music_info

  def get_current_play_time(self):
    current_play_time = self.music_player_client.get_current_play_time()
    return current_play_time['current_play_time']
