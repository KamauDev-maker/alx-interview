#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    Method that determines if a given data set represents
    """
    bytes_n = 0

    for byte in data:
        byte = byte & 0xFF

        if bytes_n > 0:
            if (byte >> 6) != 0b10:
                return False
            bytes_n -= 1
        else:
            if (byte >> 7) == 0:
                bytes_n = 0
            elif (byte >> 5) == 0b110:
                bytes_n = 1
            elif (byte >> 4) == 0b1110:
                bytes_n = 2
            elif (byte >> 3) == 0b11110:
                bytes_n = 3
            else:
                return False
    return bytes_n == 0
