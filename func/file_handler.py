from func.memory_buffer import CryptoElem
from typing import Dict, List
import json


class FileHandler:
    def __init__(self):
        self.file_path = "json_files/cipher.json"

    def crypto_object_to_dict(self, crypto: CryptoElem) -> Dict[str, str]:
        return {"message": crypto.message, "rot_type": crypto.rot_type, "crypto_type": crypto.crypto_type}

    def dict_to_crypto_object(self, dict_elem: Dict[str, str]) -> CryptoElem:
        return CryptoElem(dict_elem["message"], dict_elem["rot_type"], dict_elem["crypto_type"])

    def write_to_file(self, crypto_list: List[CryptoElem]) -> None:
        with open(self.file_path, "a") as outfile:
            json.dump([self.crypto_object_to_dict(crypto) for crypto in crypto_list], outfile)
        print(f"Buffer has been written to file: {self.file_path}")

    def read_from_file(self) -> List[CryptoElem]:
        with open(self.file_path) as json_file:
            list_of_dicts = json.load(json_file)
        print(f"Buffer has been updated from file: {self.file_path}")
        return [self.dict_to_crypto_object(crypto_dict) for crypto_dict in list_of_dicts]
