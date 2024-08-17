import sys
sys.path.append('../../')
from infrastructure.lyrics_output.lyrics_output_interface import LyricsOutputInterface
from .lyrics_output_controller_interface import LyricsOutputControllerInterface

class ConsoleController(LyricsOutputControllerInterface):
  def __init__(self, LyricsOutput: LyricsOutputInterface):
    self.lyrics_output = LyricsOutput

  def output(self, output_info):
    return self.lyrics_output.output(output_info)
