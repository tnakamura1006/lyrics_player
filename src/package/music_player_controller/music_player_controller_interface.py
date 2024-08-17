from abc import ABC, abstractmethod

class MusicPlayerControllerInterface(ABC):
  @abstractmethod
  def get_play_music_info(self):
    pass

  def get_current_play_time(self):
    pass
