import sys
sys.path.append('../../')
from infrastructure.music_player_client.music_player_client_interface import MusicPlayerClientInterface
from .music_player_controller_interface import MusicPlayerControllerInterface

class ItunesController(MusicPlayerControllerInterface):
  def __init__(self, MusicPlayerClient: MusicPlayerClientInterface):
    self.music_player_client = MusicPlayerClient

  def get_play_music_info(self):
    return self.music_player_client.get_play_music_info()
