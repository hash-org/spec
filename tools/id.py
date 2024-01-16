#!/usr/bin/env python3

"""
Generate a random string of characters.
"""

import string
import random

CHARS = string.ascii_letters + string.digits
LENGTH = 12
GENERATE = 10


def generate(length=LENGTH, chars=CHARS):
    return "hash_" + "".join(random.choice(chars) for _ in range(length))


if __name__ == "__main__":
    for _ in range(GENERATE):
        print(".. " + generate() + ":")
