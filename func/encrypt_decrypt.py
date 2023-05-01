import string
from typing import Tuple


class CryptoProcesses:
    def __init__(self, crypto_type: str):
        self.crypto_type = crypto_type
        self.alphabet = string.ascii_lowercase

    def start(self) -> Tuple[str, str]:
        message, rot_type = self.get_data_for_operation()
        returned_message = self.encrypt_decrypt_process(message, rot_type, self.crypto_type)
        return returned_message, rot_type

    def get_data_for_operation(self) -> Tuple[str, str]:
        get_data_running = True
        message = input(f"Please provide message for {self.crypto_type}: ").strip()
        rot_type = ''                            # TODO: znow, jak nie zdefiniuje czegos to podswietla w returnie
        while get_data_running:
            rot_type = input(f"What {self.crypto_type} method would you like to use ROT13 or ROT47: ").strip().lower()
            if rot_type in ['rot13', 'rot47']:
                get_data_running = False
            else:
                print("ROT type not existing, provide ROT type again.")
        return message, rot_type

    def encrypt_decrypt_process(self, message: str, rot_type: str, crypto_type) -> str:
        encrypted_message = []
        shift = int(rot_type[3:])

        if crypto_type == "decrypting":
            shift *= -1

        for letter in message:
            if letter == ' ':
                encrypted_message.append(letter)
            else:
                new_letter_index = (self.alphabet.index(letter) + shift) % len(self.alphabet)
                encrypted_message.append(self.alphabet[new_letter_index])
        final_message = ''.join(encrypted_message)
        print(f"{crypto_type.title()} finished. Message after {crypto_type}: {final_message}")
        return final_message
