from abc import ABC, abstractmethod

class MusicPlayerClientInterface(ABC):
  @abstractmethod
  def get_play_music_info(self):
    pass
