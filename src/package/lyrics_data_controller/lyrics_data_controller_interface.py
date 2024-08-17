from abc import ABC, abstractmethod

class LyricsDataControllerInterface(ABC):
  @abstractmethod
  def get_lyric(self, music_name: str, artist_name: str):
    pass
