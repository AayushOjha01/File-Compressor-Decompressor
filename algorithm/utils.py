def get_byte_array(bit_string):
    """Convert binary string to byte array"""
    # Split the string into 8-bit chunks
    byte_array = bytearray()
    for i in range(0, len(bit_string), 8):
        byte = bit_string[i:i+8]
        byte_array.append(int(byte, 2))
    return byte_array

def get_bit_string(byte_data):
    """Convert bytes to bit string"""
    bit_string = ""
    for byte in byte_data:
        # Convert each byte to binary and remove '0b' prefix, ensure 8 bits
        byte_in_binary = bin(byte)[2:].rjust(8, '0')
        bit_string += byte_in_binary
    return bit_string

def calculate_compression_stats(original_size, compressed_size):
    """Calculate and return compression statistics"""
    if original_size == 0:
        return {
            "original_size": 0,
            "compressed_size": 0,
            "compression_ratio": 0,
            "space_saving": 0
        }
        
    compression_ratio = (original_size - compressed_size) / original_size * 100
    space_saving = (1 - (compressed_size / original_size)) * 100
    
    return {
        "original_size": original_size,
        "compressed_size": compressed_size,
        "compression_ratio": round(compression_ratio, 2),
        "space_saving": round(space_saving, 2)
    }