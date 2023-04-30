class Manager:
    def __init__(self):
        self.memory= {"enc_messages": [], 'dec_messages': []}
        self.program_is_working = True

    def start(self) -> None:
        while self.program_is_working:
            choice_number = self.show_menu()
            self.execute(choice_number)

    def show_menu(self) -> int:
        print("Caesar cipher\n1. Encrypt a message\n2. Decrypt a message\n3. Exit")
        choice_number = int(input("Which action do you choose: ").strip())
        return choice_number

    def execute(self, choice_number: int) -> None:
        if choice_number == 1:
            encrypted_message = self.encrypt()
            self.memory["enc_messages"].append(encrypted_message)
        elif choice_number == 2:
            decrypted_message = self.decrypt()
            self.memory["dec_messages"].append(decrypted_message)
        elif choice_number == 3:
            self.program_is_working = False

    def encrypt(self) -> str:
        message_to_encrypt = input("Please provide message to encrypt: ").strip()
        method = int(input("What encrypting method would you like to use:\n1. ROT13\n2. ROT47: ").strip())
        alphabet = 'abcdefghijklmnoprstuwxyz'
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
                new_letter_index = (alphabet.index(letter) + shift) % len(alphabet)
                encrypted_message.append(alphabet[new_letter_index])
        print(''.join(encrypted_message))
        return ''.join(encrypted_message)

    def decrypt(self) -> str:
        message_to_decrypt = input("Please provide message to decrypt: ").strip()
        method = int(input("What decrypting method would you like to use:\n1. ROT13\n2. ROT47: ").strip())
        alphabet = 'abcdefghijklmnoprstuwxyz'
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
                new_letter_index = (alphabet.index(letter) - shift) % len(alphabet)
                decrypted_message.append(alphabet[new_letter_index])
        print(''.join(decrypted_message))
        return ''.join(decrypted_message)

    def write_to_file(self):
        pass

    def read_from_file(self):
        pass
