from package.lyrics_play_manager import LyricsPlayManager
from package.music_player_controller import ItunesController
from infrastructure.music_player_client.itunes_client import *
from package.lyrics_output_controller import ConsoleController
from infrastructure.lyrics_output.console_output import *
from package.lyrics_data_controller import JsonController
from infrastructure.data_manager.json_manager import *

if __name__ == "__main__":
  LyricsPlayManager = LyricsPlayManager(
    ItunesController(ItunesClient()),
    ConsoleController(ConsoleOutput()),
    JsonController(JsonManager()))
  LyricsPlayManager.exec()
