from encrypt_decrypt import CryptoProcesses
from dataclasses import dataclass
from typing import List
import string

cipher_ascii = \
"""      _       _               
     (_)     | |              
  ___ _ _ __ | |__   ___ _ __ 
 / __| | '_ \| '_ \ / _ \ '__|
| (__| | |_) | | | |  __/ |   
 \___|_| .__/|_| |_|\___|_|   
       | |                    
       |_|                    """


@dataclass
class Text:
    message: str
    rot_type: str
    status: str

    def __repr__(self):
        pass


class Buffer:
    memory: List[Text] = []


class Manager:
    def __init__(self):
        self.memory = Buffer()
        self.program_is_working = True
        self.alphabet = string.ascii_lowercase

    def start(self) -> None:
        while self.program_is_working:
            choice_number = self.show_menu()
            self.execute(choice_number)

    def get_input(self):
        choice_number = int(input("Which action do you choose: ").strip())
        if choice_number in range(1, 8):
            return choice_number
        else:
            print(f"Provided option: {choice_number}, not such option. Choose again.\n")

    def show_menu(self) -> int:
        run_menu = True
        choice_number = 0  # PYTANIE, czy tak to tutaj mam dołożyć? jak nie ma to podswietla return
        print("*" * 31)
        print(cipher_ascii)
        print("*" * 31)
        while run_menu:
            print("1. Encrypt a message\n2. Decrypt a message\n3. Show memory buffer\n4. Clear memory buffer\n"
                  "5. Write buffer to file\n6. Read file to memory buffer\n7. Exit")
            try:
                choice_number = self.get_input()
                run_menu = False
            except ValueError:
                print("Please provide number instead of string.\n")
        return choice_number

    def execute(self, choice_number: int) -> None:
        match choice_number:
            case 1:
                crypto_process = CryptoProcesses("encrypting")
                crypto_process.start()
                # stworzenie obiektu dataclass
                # wykonanie enkrypcji z pobraniem info od uzytkownika
                # zapisanie do buffera
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                print("Good bye!")
                self.program_is_working = False

        # if choice_number == 1:
        #     encrypted_message = self.encrypt()
        #     self.memory["enc_messages"].append(encrypted_message)
        # elif choice_number == 2:
        #     decrypted_message = self.decrypt()
        #     self.memory["dec_messages"].append(decrypted_message)
        # elif choice_number == 3:
        #     self.program_is_working = False

