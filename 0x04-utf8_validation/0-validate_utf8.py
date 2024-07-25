def validUTF8(data):
    # Helper function to check if a byte is a valid continuation byte
    def is_continuation(byte):
        return byte >> 6 == 0b10

    # Iterate through the data
    i = 0
    while i < len(data):
        # Get the number of bytes for this character
        first_byte = data[i] & 0xFF  # Ensure we only consider the 8 least significant bits
        if first_byte >> 7 == 0:  # 1-byte character
            bytes_count = 1
        elif first_byte >> 5 == 0b110:  # 2-byte character
            bytes_count = 2
        elif first_byte >> 4 == 0b1110:  # 3-byte character
            bytes_count = 3
        elif first_byte >> 3 == 0b11110:  # 4-byte character
            bytes_count = 4
        else:
            return False  # Invalid first byte

        # Check if we have enough bytes
        if i + bytes_count > len(data):
            return False

        # Validate continuation bytes
        for j in range(1, bytes_count):
            if not is_continuation(data[i + j] & 0xFF):
                return False

        i += bytes_count

    return True
