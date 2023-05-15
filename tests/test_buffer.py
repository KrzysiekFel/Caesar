from func.memory_buffer import Buffer, CryptoElem


class TestBuffer:
    def setup_method(self):
        self.buffer = Buffer()

    def test_should_clear_buffer_when_memory_consists_elements(self):
        test_elem_crypto = CryptoElem("test_message", "test_rot_type", "test_crypto_type")
        self.buffer.memory.append(test_elem_crypto)
        self.buffer.clear_memory_buffer()
        assert self.buffer.memory == []
