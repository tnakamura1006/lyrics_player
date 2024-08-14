import time
from .lyrics_output_interface import LyricsOutputInterface

class LyricsConsoleOutput(LyricsOutputInterface):
  def __init__(self):
    pass

  def output(self, output_info: dict):
    print(output_info)
