# Bluecrypt

Bluecrypt is a cryptographic algorithm created for my second year cryptography assignment.

The assignment is to create a cryptographic algorithm for extreme IoT devices. The main assumptions are:

 - Low computational power
 - Low memory
 - No trusted third party (optional)

The algorithm should provide encryption, a key exchange method, integrity checking and certification (optional).

## Algorithm Implementations
This algorithm takes the assumptions into consideration and uses the Diffie-Hellman Protocol to generate a mathematically secure encryption and decryption key between two parties without trusting a third party with the key.

The key is used to encrypt data with a stream cipher as stream ciphers use considerably less processing power and memory than a block cipher.

Although existing algorithms are used, the code was solely written and tested by me.

Created for:
University of Gloucestershire - Cryptography CT5046, Assignment 1.

### Diffie-Hellman Flowchart
![Diffie-Hellman Algorithm](https://i.imgur.com/QyLg9vE.png)
### Bluecrypt Flowchart
![Bluecrypt Algorithm](https://i.imgur.com/C89AhRU.png)
## Installation

No external modules are required for this script as it uses the Python 3 standard library. To download the code please type the following into the terminal.

```bash
git clone https://github.com/bgr-github/Bluecrypt
```

## Usage

```python
import diffiehellman as DH
from streamcipher import encrypt, decrypt

GENERATOR = 16
PRIME = 74708507604228654606572203229598384855739981161883502863734464

# Generate public key
private_key = 12345
public_key = DH.generate_public_key(GENERATOR, private_key, PRIME)
>>> "72394577518043085212216035861441461394798169043826752960806400"

# Generate encryption key
key = DH.generate_encryption_key(private_key, int(public_key), PRIME)
>>> "55745170060049986791727709982738755425000447966583397548786304"

# Encrypt data (returns hex value as list)
cipher = encrypt(str(key), "Hello this is the data")
>>> ['48', '65', '6c', '6c', '6f', '20', '74', '68', '69', '73', '20', '69', '73', '20', '74', '68', '65', '20', '64', '61', '74', '61']

decrypt(str(key), cipher)
>>> "Hello this is  the data"""
```

## Contributing

I am not looking for contributions to this repository, but I would love to see improvements, forking this repo is highly encouraged :)

## License

[MIT](https://choosealicense.com/licenses/mit/)
