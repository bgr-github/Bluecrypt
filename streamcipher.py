import codecs
from typing import List

# The modulo for the key scheduling and random number generation.
MOD = 256


def encrypt(key: str, plaintext: str) -> List[str]:
    """Encrypts the data."""
    return logic(key, [ord(c) for c in plaintext])


def decrypt(key: str, ciphertext: str) -> str:
    """Decrypts the data."""
    ciphertext = codecs.decode(ciphertext, "hex_codec")
    result = logic(key, ciphertext)
    return codecs.decode(result, "hex_codec").decode("utf-8")


def logic(key: str, text):
    """The logic behind the encryption and decryption process."""
    key = [ord(c) for c in key]
    result = []

    for c in text:
        # XOR the data and convert the characters to hexadecimal.
        val = format((c ^ next(keystream(key))), "02x")
        result.append(val)

    return "".join(result)


def key_schedule(key: str) -> List[int]:
    """Key Scheduling Algorithm"""
    s = [i for i in range(MOD)]
    j = 0
    for i in range(MOD):
        j = (j + s[i] + int(key[i % len(key)])) % MOD
        s[i], s[j] = s[j], s[i]

    return s


def random_number(s: List[int]) -> int:
    """Generates a Pseudo-random number for the keystream"""
    i, j = 0, 0

    while True:
        i = (i + 1) % MOD
        j = (j + s[i]) % MOD

        # Value swapping
        s[i], s[j] = s[j], s[i]

        # Yield the next bit in the key
        # Yield is similar to return but transforms the result into an iterator (generator)
        yield s[(s[i] + s[j]) % MOD]


def keystream(key: str) -> int:
    """Returns the result of a random number with the parameter of the KSA."""
    return random_number(key_schedule(key))
