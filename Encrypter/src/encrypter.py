from cryptography.fernet import Fernet

def encrypt_file(file, key_file=None):
    '''Creates an encrypted copy of a file using Fernet (symmetric encryption) in the working directory.
    The function takes a file as main argument and a key_file as optional argument. If no key_file
    is given, then a key for the encryption is created using Fernet.generate_key()'''

    if key_file != None:
        with open(key_file, 'rb') as filekey:
            key = filekey.read()
    else:
        key = Fernet.generate_key() # key generation

        # string the key in a file
        with open('my_key.key', 'wb') as filekey:
            filekey.write(key)

    fernet = Fernet(key) # using the generated key

    # opening the original file to encrypt
    with open(file, 'rb') as file:
        original = file.read()

    # encrypting the file
    encrypted = fernet.encrypt(original)

    file_name = str(file.name)+'_encrypted'

    # opening the file in write mode and writing the encrypted data
    with open(file_name, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
