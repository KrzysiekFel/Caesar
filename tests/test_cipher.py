from func.encrypt_decrypt import CryptoProcesses
from func.memory_buffer import Buffer, CryptoElem
from func.file_handler import FileHandler
from unittest.mock import patch, mock_open
import pytest


class TestEncryptProcess:
    def setup_method(self):
        self.crypto_process = CryptoProcesses("encrypting")

    @pytest.mark.parametrize("message, result", [("Kris5 10", "Xevf5 10"),
                                                 ("    2023 starts NOW!", "    2023 fgnegf ABJ!"),
                                                 ("AbCdEf   123&", "NoPqRs   123&")])
    def test_should_return_correctly_encrypted_message_for_rot13(self, message, result):
        final_message = self.crypto_process.encrypt_decrypt_process(message, "ROT13", self.crypto_process.crypto_type)
        assert final_message == result

    @pytest.mark.parametrize("message, result", [("ABC  123 abc", "VWX  123 vwx"),
                                                 ("    XxYyZz!", "    SsTtUu!"),
                                                 ("    2023 starts NOW!", "    2023 novmon IJR!")])
    def test_should_return_correctly_encrypted_message_for_rot47(self, message, result):
        final_message = self.crypto_process.encrypt_decrypt_process(message, "ROT47", self.crypto_process.crypto_type)
        assert final_message == result


class TestDecryptProcess:
    def setup_method(self):
        self.crypto_process = CryptoProcesses("decrypting")

    @pytest.mark.parametrize("message, result", [("Xevf5 10", "Kris5 10"),
                                                 ("    2023 fgnegf ABJ!", "    2023 starts NOW!"),
                                                 ("NoPqRs   123&", "AbCdEf   123&")])
    def test_should_return_correctly_decrypted_message_for_rot13(self, message, result):
        final_message = self.crypto_process.encrypt_decrypt_process(message, "ROT13", self.crypto_process.crypto_type)
        assert final_message == result

    @pytest.mark.parametrize("message, result", [("VWX  123 vwx", "ABC  123 abc"),
                                                 ("    SsTtUu!", "    XxYyZz!"),
                                                 ("    2023 novmon IJR!", "    2023 starts NOW!")])
    def test_should_return_correctly_decrypted_message_for_rot47(self, message, result):
        final_message = self.crypto_process.encrypt_decrypt_process(message, "ROT47", self.crypto_process.crypto_type)
        assert final_message == result


class TestBuffer:
    def setup_method(self):
        self.buffer = Buffer()

    def test_should_clear_buffer_when_memory_consists_elements(self):
        test_elem_crypto = CryptoElem("test_message", "test_rot_type", "test_crypto_type")
        self.buffer.memory.append(test_elem_crypto)
        self.buffer.clear_memory_buffer()
        assert self.buffer.memory == []


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
        with patch("builtins.open", mock_open()) as mock_file:
            self.handler.write_to_file(crypto_list, "test_file")
            mock_file.assert_called_once_with(self.fake_file_path, 'a')
            mock_file().write.assert_called_once_with(self.file_cont)
