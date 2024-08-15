import math
import sys
from .music_player_controller_interface import MusicPlayerControllerInterface
sys.path.append('../../')
from infrastructure.music_player_client.itunes_client import ItunesClient

class ItunesController(MusicPlayerControllerInterface):
  def __init__(self):
    self.itunes_client = ItunesClient()

  def get_play_music_info(self):
    return self.itunes_client.get_play_music_info()
