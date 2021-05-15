# Encrypter

Creates an encrypted copy of a file using Fernet (symmetric encryption) in the working directory.
    The function takes a file as main argument and a key_file as optional argument. If no key_file
    is given, then a key for the encryption is created using Fernet.generate_key()

## Installation
To install run the following:
```python
pip install encrypter
```

## Usage
``` python
from encrypter import encrypt_file

# generate key and encrypted copy of my_file in the working directory
encrypt_file('my_file')
```
