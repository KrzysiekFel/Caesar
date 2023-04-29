class Manager:
    def __init__(self):
        self.memory_buffer = []
        self.program_is_working = True

    def start(self):
        while self.program_is_working:
            self.show_menu()
            self.execute()

    def show_menu(self):
        pass

    def execute(self):
        pass

    def encrypt(self, message: str, method: str) -> str:
        alphabet = 'abcdefghijklmnoprstuwxyz'
        encrypted_message = []
        method = method.strip().lower()

        if method == 'rot13':
            shift = 13
        elif method == 'rot47':
            shift = 47
        else:
            raise NotImplementedError

        for letter in message:
            if letter == ' ':
                encrypted_message.append(letter)
            else:
                new_letter_index = (alphabet.index(letter) + shift) % len(alphabet)
                encrypted_message.append(alphabet[new_letter_index])
        return ''.join(encrypted_message)

    def decrypt(self, message: str, method: str) -> str:
        pass
