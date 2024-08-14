import math
from .music_player_controller_interface import MusicPlayerControllerInterface
from .itunes_service import ItunesService

class ItunesController(MusicPlayerControllerInterface):
  def __init__(self):
    self.itunes_service = ItunesService()

  def get_play_music_info(self):
    return self.itunes_service.get_play_music_info()
