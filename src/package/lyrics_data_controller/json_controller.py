import sys
sys.path.append('../../')
from infrastructure.data_manager.data_manager_interface import DataManagerInterface
from .lyrics_data_controller_interface import LyricsDataControllerInterface

class JsonController(LyricsDataControllerInterface):
  def __init__(self, DataManager: DataManagerInterface):
    self.data_manager = DataManager

  def get_lyric(self, music_name: str, artist_name: str):
    file_name = 'test/' + music_name + '_' + artist_name + '.json'  # ディレクトリはconfigで設定させる
    return self.data_manager.get_data(file_name)
