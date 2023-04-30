from manager import Manager
import pytest


class TestEncrypt:
    def test_should_return_correctly_encrypted_message_for_rot13(self, mocker):
        manager = Manager()
        mocker.patch('builtins.input', return_value='abc')
        mocker.patch('builtins.input', return_value='1')
        assert manager.encrypt() == 'nop'


class TestDecrypt:
    pass


class TestShowMenu:
    @pytest.mark.parametrize("input_value, returned_value", [('1', 1), ('2', 2), ('3', 3)])
    def test_should_return_correct_number_when_user_enter_correct_option(self, input_value, returned_value, mocker):
        mocker.patch('builtins.input', return_value=input_value)
        manager = Manager()
        assert manager.show_menu() == returned_value

    def test_show_menu_invalid_input(self, mocker):
        manager = Manager()
        mocker.patch('builtins.input', return_value='4')
        expected_output = 'Provided option: 4, not such option. Choose again.\n\n' \
                          '1. Encrypt a message\n2. Decrypt a message\n3. Exit\n\n' \
                          'Which action do you choose: '

        assert manager.show_menu() == expected_output

    def test_should_return_nothing_when_user_enter_letter_instead_number(self):
        pass


