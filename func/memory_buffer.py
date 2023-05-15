from dataclasses import dataclass
from typing import List


@dataclass
class CryptoElem:
    message: str
    rot_type: str
    crypto_type: str


class Buffer:
    """
    Class for handling memory buffer.
    """
    memory: List[CryptoElem] = []

    def show_memory_buffer(self) -> None:
        """
        Printing memory buffer to user.
        """
        print("Printing current memory buffer.")
        print('=' * 42)
        print(f"{'MESSAGE:': <18}{'AFTER:': <15}{'ROT TYPE:': <15}")
        for crypto_elem in Buffer.memory:
            print(f"{crypto_elem.message: <18}{crypto_elem.crypto_type: <15}{crypto_elem.rot_type: <15}")
        print('=' * 42)

    def clear_memory_buffer(self) -> None:
        """
        Clearing memory buffer.
        """
        Buffer.memory.clear()
        print("Memory buffer has been cleared.")
