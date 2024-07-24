#!/usr/bin/python3
""" Determines if a given data set represents a valid UTF-8 encoding. """
from itertools import takewhile


def int_to_bytes(nums):
    """ Helper function that converts ints to bits """
    for num in nums:
        bytes = []
        mask = 1 << 8
        while mask:
            mask >>= 1
            bytes.append(bool(num & mask))
        yield bytes


def validUTF8(data):
    """ Initialize a variable to keep track of the
    number of bytes expected.
    """
    num_bytes = int_to_bytes(data)

    """ Iterate through each integer in the data """
    for byte in num_bytes:
        """ Check if the most significant bit (MSB)
         is 0 (single-byte character) """
        # If single byte char, then valid..
        if byte[0] == 0:
            continue

        # At this point, byte is a multi-byte char
        units = sum(takewhile(bool, byte))
        if units <= 1:  # UTF-8 can be 1 to 4 bytes long
            return False
        if units >= 4:
            return False

        for _ in range(units - 1):
            """ Check if the next byte starts with 10
            (continuation byte). """
            try:
                byte = next(num_bytes)
            except StopIteration:
                return False
            if byte[0] != 1 or byte[1] != 0:
                return False
    return True
