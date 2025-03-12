class FileHandler:
    """Handles file operations for Huffman coding"""
    
    @staticmethod
    def read_file(file_path):
        """Read file and return its content"""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except Exception as e:
            raise IOError(f"Error reading file: {e}")
    
    @staticmethod
    def write_compressed_file(output_path, byte_array):
        """Write compressed data to binary file"""
        try:
            with open(output_path, 'wb') as file:
                file.write(bytes(byte_array))
            return True
        except Exception as e:
            raise IOError(f"Error writing compressed file: {e}")
    
    @staticmethod
    def read_compressed_file(file_path):
        """Read compressed binary file and return byte data"""
        try:
            with open(file_path, 'rb') as file:
                byte_data = file.read()
            return byte_data
        except Exception as e:
            raise IOError(f"Error reading compressed file: {e}")
    
    @staticmethod
    def write_decompressed_file(output_path, text):
        """Write decompressed text to file"""
        try:
            with open(output_path, 'w', encoding='utf-8') as file:
                file.write(text)
            return True
        except Exception as e:
            raise IOError(f"Error writing decompressed file: {e}")
    
    @staticmethod
    def save_codes(file_path, codes):
        """Save Huffman codes to a file"""
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                for char, code in codes.items():
                    # Store character as ascii value to handle all characters
                    if char == '\n':
                        char_ascii = 'newline'
                    else:
                        char_ascii = ord(char)
                    file.write(f"{char_ascii}:{code}\n")
            return True
        except Exception as e:
            raise IOError(f"Error saving codes: {e}")
    
    @staticmethod
    def load_codes(file_path):
        """Load Huffman codes from a file"""
        codes = {}
        reverse_mapping = {}
        
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue
                    
                    char_ascii, code = line.split(':')
                    
                    if char_ascii == 'newline':
                        char = '\n'
                    else:
                        char = chr(int(char_ascii))
                    
                    codes[char] = code
                    reverse_mapping[code] = char
                    
            return codes, reverse_mapping
        except Exception as e:
            raise IOError(f"Error loading codes: {e}")