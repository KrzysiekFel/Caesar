

class CryptoProcesses:
    def __init__(self, encrypt_type: str):
        self.encrypt_type = encrypt_type

    def start(self):
        message, rot_type = self.get_data_for_operation()
        if self.encrypt_type == "encrypting":
            self.encrypt(message, rot_type)
        else:
            self.decrypt(message, rot_type)

    def get_data_for_operation(self):
        message = input(f"Please provide message for {self.encrypt_type}: ").strip()
        rot_type = input(f"What {self.encrypt_type} method would you like to use: ROT13 or ROT47: ").strip().lower()
        return message, rot_type

    def encrypt(self, message: str, rot_type: str) -> str:
        encrypted_message = []

        if method == 1:
            shift = 13
        elif method == 2:
            shift = 47
        else:
            raise NotImplementedError

        for letter in message_to_encrypt:
            if letter == ' ':
                encrypted_message.append(letter)
            else:
                new_letter_index = (self.alphabet.index(letter) + shift) % len(self.alphabet)
                encrypted_message.append(self.alphabet[new_letter_index])
        print(''.join(encrypted_message))
        return ''.join(encrypted_message)

    def decrypt(self, message: str, rot_type: str) -> str:
        decrypted_message = []

        if method == 1:
            shift = 13
        elif method == 2:
            shift = 47
        else:
            raise NotImplementedError

        for letter in message_to_decrypt:
            if letter == ' ':
                decrypted_message.append(letter)
            else:
                new_letter_index = (self.alphabet.index(letter) - shift) % len(self.alphabet)
                decrypted_message.append(self.alphabet[new_letter_index])
        print(''.join(decrypted_message))
        return ''.join(decrypted_message)
