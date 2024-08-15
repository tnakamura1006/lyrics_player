import sys
sys.path.append('../../')
from infrastructure.lyrics_output.lyrics_output_interface import LyricsOutputInterface

class LyricsOutputController():
  def __init__(self, LyricsOutput: LyricsOutputInterface):
    self.lyrics_output = LyricsOutput

  def output(self):
    return self.lyrics_output.output()
