from abc import ABC, abstractmethod

class MusicPlayerClientInterface(ABC):
  @abstractmethod
  def get_current_track(self):
    pass

  def get_music_player_status(self):
    pass

  def get_current_play_time(self):
    pass
