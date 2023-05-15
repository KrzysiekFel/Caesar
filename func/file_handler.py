from .memory_buffer import CryptoElem
from typing import Dict, List
import json


class FileHandler:
    """
    Class for handling file (saving/loading).
    """
    def __init__(self):
        self.folder_path = "json_files/"

    @staticmethod
    def get_file_name() -> str:
        """
        Getting file name input from user.
        :return: file name
        """
        file_name = input("Please provide file name for /Caesar/json_files/<file_name>.json: ").strip()
        return file_name

    def write_to_file(self, crypto_list: List[CryptoElem], file_name: str) -> None:
        """
        Writing encrypted and decrypted elements to json file.
        :param crypto_list: list of Crypto objects
        :param file_name: name of json file
        """
        file_path = self.folder_path + file_name + ".json"
        result = {"memory_buffer": [crypto.__dict__ for crypto in crypto_list]}
        with open(file_path, "a") as outfile:
            json.dump(result, outfile)
        print(f"Buffer has been written to: {file_path}")

    def read_from_file(self, file_name: str) -> List[CryptoElem]:
        """
        Reading encrypted and decrypted elements from declared json file to memory buffer.
        :param file_name: name of json file
        :return: list of Crypto objects
        """
        file_path = self.folder_path + file_name + ".json"
        with open(file_path) as json_file:
            loaded_json_dict = json.load(json_file)
        list_of_dicts = loaded_json_dict["memory_buffer"]
        print(f"Buffer has been updated from: {file_path}")
        return [CryptoElem(**crypto_dict) for crypto_dict in list_of_dicts]
