from abc import ABC, abstractmethod

class DataManagerInterface(ABC):
  @abstractmethod
  def get_data(self, file_name: str):
    pass
