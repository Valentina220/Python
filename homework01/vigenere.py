def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    # PUT YOUR CODE HERE
    #m = plaintext
    #k = keyword
    keyword *= len(plaintext) // len(keyword) + 1
    for i, j in enumerate(plaintext):
        if ord('A') <= ord(j) <= ord('Z'):
            code = (ord(j) + ord(keyword[i]))
            ciphertext += chr(code % 26 + 65)
            print(ciphertext)
        elif ord('a') <= ord(j) <= ord('z'):
            code = (ord(j) + ord(keyword[i]))
            ciphertext += chr(code % 26 + 97)
            print(ciphertext)
        elif ord(j) == 32:
            ciphertext += chr(32)
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    # PUT YOUR CODE HERE
    keyword *= len(ciphertext) // len(keyword) + 1
    for i, j in enumerate(ciphertext):
        if ord('A') <= ord(j) <= ord('Z'):
            code = (ord(j) - ord(keyword[i]))
            plaintext += chr(code % 26 + 65)
        elif ord('a') <= ord(j) <= ord('z'):
            code = (ord(j) - ord(keyword[i]))
            plaintext += chr(code % 26 + 97)
        elif ord(j) == 32:
            plaintext += chr(32)
    return plaintext
