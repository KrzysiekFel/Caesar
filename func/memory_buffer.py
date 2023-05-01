from dataclasses import dataclass
from typing import List


@dataclass
class CryptoElem:
    message: str
    rot_type: str
    crypto_type: str

    def __repr__(self) -> str:
        return f"{self.message: <18}{self.crypto_type: <15}{self.rot_type: <15}"


class Buffer:
    memory: List[CryptoElem] = []

    def show_memory_buffer(self) -> None:
        print("Printing current memory buffer.")
        print('=' * 42)
        print(f"{'MESSAGE': <18}{'AFTER': <15}{'ROT TYPE': <15}")
        for crypto_elem in self.memory:
            print(crypto_elem)
        print('=' * 42)

    def clear_memory_buffer(self) -> None:
        self.memory = []
        print("Memory buffer has been cleared.")