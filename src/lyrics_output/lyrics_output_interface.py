from abc import ABC, abstractmethod

class LyricsOutputInterface(ABC):
  @abstractmethod
  def output(self, output_info: str):
    pass
