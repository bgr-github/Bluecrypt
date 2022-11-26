#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""bluecrypt.py:
    An algorithm which uses the Diffie-Hellman Protocol and the RC4 algorithm to trasfer data between extreme IoT devices.
    The assumptions for the IoT devices are that they run from very limited processing power and memory, so a stream cipher was
    implemented as they require lower processing power than block ciphers. RC4 is very insecure to use, but has been used in this
    algorithm as it fits the use case speed-wise and as I am not a mathematics student, it is still very secure compared to a cipher algorithm
    which I would design at this moment in time.


    * Although existing algorithms are implemented, all code has been written and tested by myself (George Beager).
    * This Python file uses static typing, so the syntax will differ from "vanilla" Python code. However, this is part 
      of the standard library, so no additional modules are needed.

    Modules required:
        * No installs are required as this script only uses the Python 3 standard library.

    Created for:
        University of Gloucestershire - Cryptography CT5046, Assignment 1.
"""

__author__  = "George Beager"


import json
import diffiehellman as dh
from streamcipher import encrypt, decrypt
from types import SimpleNamespace as Namespace


# Large prime number
P = 74708507604228654606572203229598384855739981161883502863734464

# Generator: (ideally primitive root of a prime number for max security)
G = 16


def main() -> None:
    """Runs the main Python script"""

    # Generate a private and public key for the temperature sensor.
    sensor = Namespace(private_key=82645)
    sensor.public_key = dh.generate_public_key(G, sensor.private_key, P)

    # Generate a private and public key for the HVAC system.
    hvac = Namespace(private_key=30924)
    hvac.public_key = dh.generate_public_key(G, hvac.private_key, P)

    # Generate an encryption key. sensor is sending data to hvac- therefore uses his public key for him to decrypt.
    sensor_encryption_key = dh.generate_encryption_key(sensor.private_key, int(hvac.public_key), P)

    # Serialize mock data to bytes form to be encrypted and sent over the network.
    unencrypted_json = json.dumps({
        "current_temp": 18.0,
        "desired_temp": 21.0,
    })

    # Encrypt the serialized data
    cipher: str = encrypt(str(sensor_encryption_key), unencrypted_json)

    # Creating a dictionary to act like a packet being sent across a network.
    packet = {
        "prime": P,
        "generator": G,
        "public_key": sensor.public_key,
        "data": cipher
    }

    """Reads the packet and decrypts it, exactly like the receiving machine would."""
    recv_data = packet
    hvac_encryption_key = dh.generate_encryption_key(hvac.private_key, int(recv_data["public_key"]), recv_data["prime"])

    print("HVAC Decrypts: ")
    print(decrypt(hvac_encryption_key, recv_data["data"]))


if __name__ == "__main__":
    main()
