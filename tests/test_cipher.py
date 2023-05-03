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


