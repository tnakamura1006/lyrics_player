from abc import ABC, abstractmethod

class LyricsOutputInterface(ABC):
  @abstractmethod
  def output(self):
    pass
