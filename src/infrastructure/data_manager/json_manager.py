import json
from .data_manager_interface import DataManagerInterface

class JsonManager(DataManagerInterface):
  def __init__(self):
    pass

  def get_data(self, file_name: str):
    try:
      with open(file_name, 'r', encoding='utf-8') as file:
        return json.load(file)
    except Exception as e:
      # print(f"An unexpected error occurred: {e}")
      return None
