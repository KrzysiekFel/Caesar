from func.file_handler import FileHandler
from func.memory_buffer import CryptoElem
from unittest.mock import patch, mock_open
import json
from tempfile import NamedTemporaryFile


class TestFileHandler:
    def setup_method(self):
        self.handler = FileHandler()
        self.fake_file_path = "json_files/test_file.json"
        self.file_cont = '{"memory_buffer": ' \
                         '[{"message": "test1", "rot_type": "rot13", "crypto_type": "encrypting"}, ' \
                         '{"message": "test2", "rot_type": "rot47", "crypto_type": "decrypting"}]} '

    def test_should_return_list_of_objects_when_reading_from_json_file(self):
        with patch("builtins.open", mock_open(read_data=self.file_cont)) as mock_file:
            crypto_list = self.handler.read_from_file("test_file")
            mock_file.assert_called_once_with(self.fake_file_path)
            assert len(crypto_list) == 2
            assert crypto_list[0].message == "test1"
            assert crypto_list[0].rot_type == "rot13"
            assert crypto_list[0].crypto_type == "encrypting"
            assert crypto_list[1].message == "test2"
            assert crypto_list[1].rot_type == "rot47"
            assert crypto_list[1].crypto_type == "decrypting"

    def test_should_correctly_write_memory_buffer_to_json_file(self):
        crypto_list = [CryptoElem("test1", "rot13", "encrypting"), CryptoElem("test2", "rot47", "decrypting")]
        with NamedTemporaryFile() as temp_file:
            file_path = temp_file.name
            self.handler.folder_path = ""
            self.handler.write_to_file(crypto_list, file_path)
            with open(file_path) as f:
                content = json.load(f)
                assert content == self.file_cont

