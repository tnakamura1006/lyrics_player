from abc import ABC, abstractmethod

class LyricsOutputControllerInterface(ABC):
  @abstractmethod
  def output(self, output_info):
    pass
