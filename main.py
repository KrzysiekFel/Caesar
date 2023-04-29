def encrypt(message: str, method: str) -> str:
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


def decrypt(message: str, method: str) -> str:
    pass


def main():
    print(encrypt('abc xyz', 'rot13'))
    print(encrypt('abc xyz', 'rot47'))


if __name__ == '__main__':
    main()



# TODO: encrypt method
# TODO: decrypt method
# TODO: file handler
# TODO: datasclass
