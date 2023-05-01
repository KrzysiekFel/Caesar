from func.encrypt_decrypt import CryptoProcesses
from func.memory_buffer import CryptoElem, Buffer

cipher_ascii = \
"""      _       _               
     (_)     | |              
  ___ _ _ __ | |__   ___ _ __ 
 / __| | '_ \| '_ \ / _ \ '__|
| (__| | |_) | | | |  __/ |   
 \___|_| .__/|_| |_|\___|_|   
       | |                    
       |_|                    """


class Manager:
    def __init__(self):
        self.buffer = Buffer()
        self.program_is_working = True

    def start(self) -> None:
        print("*" * 31)
        print(cipher_ascii)
        while self.program_is_working:
            choice_number = self.show_menu()
            self.execute(choice_number)

    def get_input(self) -> int:
        choice_number = int(input("Which action do you choose: ").strip())
        if choice_number in range(1, 8):
            return choice_number
        else:
            print(f"Provided option: {choice_number}, not such option. Choose again.")

    def show_menu(self) -> int:
        run_menu = True
        choice_number = 0                 # TODO: czy tak to tutaj mam dołożyć? jak nie ma to podswietla return
        while run_menu:
            print("*" * 31)
            print("1. Encrypt a message\n2. Decrypt a message\n3. Show memory buffer\n4. Clear memory buffer\n"
                  "5. Write buffer to file\n6. Read file to memory buffer\n7. Exit")
            try:
                choice_number = self.get_input()
                run_menu = False
            except ValueError:
                print("Please provide number instead of string.")
        return choice_number

    def execute(self, choice_number: int) -> None:
        match choice_number:
            case 1:
                crypto_type = "encrypting"
                self.crypto_execution(crypto_type)
            case 2:
                crypto_type = "decrypting"
                self.crypto_execution(crypto_type)
            case 3:
                self.buffer.show_memory_buffer()
            case 4:
                self.buffer.clear_memory_buffer()
            case 5:
                pass
            case 6:
                pass
            case 7:
                print("Good bye!")
                self.program_is_working = False

    def crypto_execution(self, crypto_type: str) -> None:
        crypto_process = CryptoProcesses(crypto_type)
        final_message, rot_type = crypto_process.start()
        crypto_elem = CryptoElem(final_message, rot_type, crypto_type)
        self.buffer.memory.append(crypto_elem)
        print("Message added to memory buffer.")

