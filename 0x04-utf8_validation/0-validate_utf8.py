#!/usr/bin/python3
""" Determines if a given data set represents a valid UTF-8 encoding. """


def validUTF8(data):
    """ Initialize a variable to keep track of the
    number of bytes expected.
    """
    num_bytes = 0

    """ Iterate through each integer in the data """
    for byte in data:
        """ Check if the most significant bit (MSB)
         is 0 (single-byte character) """
        if num_bytes == 0:
            if byte >> 7 == 0b0:
                continue
            elif byte >> 5 == 0b110:
                num_bytes = 1
            elif byte >> 4 == 0b1110:
                num_bytes = 2
            elif byte >> 3 == 0b11110:
                num_bytes = 3
            else:
                """ Check if the next byte starts with 10
                (continuation byte). """
                if byte >> 6 != 0b10:
                    return False
                num_bytes -= 1

    return num_bytes == 0
