from abc import ABC, abstractmethod

class MusicPlayerControllerInterface(ABC):
  @abstractmethod
  def get_play_music_info(self):
    pass
