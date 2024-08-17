from .lyrics_output_interface import LyricsOutputInterface

class ConsoleOutput(LyricsOutputInterface):
  def __init__(self):
    pass

  def output(self, output_info):
    print(output_info)
