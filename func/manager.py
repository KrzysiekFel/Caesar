from func.encrypt_decrypt import CryptoProcesses
from func.memory_buffer import CryptoElem, Buffer
from func.file_handler import FileHandler

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
    """
    Class for handling program.
    """
    def __init__(self):
        self.buffer = Buffer()
        self.file_handler = FileHandler()
        self.program_is_working = True
        self.available_choices = {1: "Encrypt a message", 2: "Decrypt a message", 3: "Show memory buffer",
                                  4: "Clear memory buffer", 5: "Write buffer to file", 6: "Read file to memory buffer",
                                  7: "Exit"}

    def start(self) -> None:
        """
        Executing user choices.
        """
        print("*" * 31)
        print(cipher_ascii)
        while self.program_is_working:
            choice_number = self.show_menu()
            self.execute(choice_number)

    def get_input(self) -> int:
        """
        Getting chosen action input from user.
        :return: choice number
        """
        choice_number = int(input("Which action do you choose: ").strip())
        if choice_number in self.available_choices.keys():
            return choice_number
        else:
            print(f"Provided option: {choice_number}, not such option. Choose again.")

    def show_menu(self) -> int:
        """
        Showing menu.
        :return: chosen action
        """
        run_menu = True
        choice_number = 0
        while run_menu:
            print("*" * 31)
            for key, value in self.available_choices.items():
                print(f"{key}. {value}")
            try:
                choice_number = self.get_input()
                run_menu = False
            except ValueError:
                print("Please provide number instead of string.")
        return choice_number

    def execute(self, choice_number: int) -> None:
        """
        Execute chosen action.
        :param choice_number
        """
        match choice_number:
            case 1:
                self.crypto_execution("encrypting")
            case 2:
                self.crypto_execution("decrypting")
            case 3:
                self.buffer.show_memory_buffer()
            case 4:
                self.buffer.clear_memory_buffer()
            case 5:
                file_name = self.file_handler.get_file_name()
                self.file_handler.write_to_file(self.buffer.memory, file_name)
            case 6:
                file_name = self.file_handler.get_file_name()
                for crypto_object in self.file_handler.read_from_file(file_name):
                    self.buffer.memory.append(crypto_object)
            case 7:
                print("Good bye!")
                self.program_is_working = False

    def crypto_execution(self, crypto_type: str) -> None:
        """
        Method for executing encryption or decryption and saving result to buffer.
        :param crypto_type: encrypting or decrypting
        """
        crypto_process = CryptoProcesses(crypto_type)
        final_message, rot_type = crypto_process.start()
        crypto_elem = CryptoElem(final_message, rot_type, crypto_type)
        self.buffer.memory.append(crypto_elem)
        print("Message added to memory buffer.")
