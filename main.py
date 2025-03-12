import os
from huffman.core import HuffmanCore
from huffman.utils import get_byte_array, get_bit_string, calculate_compression_stats
from file_io.file_handler import FileHandler
from file_io.cli import CLI

class HuffmanCoding:
    """Main class for Huffman coding application"""
    
    def __init__(self):
        """Initialize the Huffman coding application"""
        self.file_handler = FileHandler()
        self.cli = CLI()
    
    def compress(self, input_path, output_path=None):
        """Compress a file using Huffman coding"""
        try:
            # Set default output path if not provided
            if output_path is None:
                output_path = input_path + ".bin"
            
            # Read input file
            text = self.file_handler.read_file(input_path)
            if not text:
                print("File is empty. Nothing to compress.")
                return None
            
            # Build frequency table
            frequency_table = HuffmanCore.build_frequency_table(text)
            
            # Build Huffman tree
            root = HuffmanCore.build_huffman_tree(frequency_table)
            if root is None:
                print("Failed to build Huffman tree.")
                return None
            
            # Generate codes
            codes, reverse_mapping = HuffmanCore.generate_codes(root)
            
            # Encode text
            encoded_text = HuffmanCore.encode_text(text, codes)
            
            # Pad encoded text
            padded_text = HuffmanCore.pad_encoded_text(encoded_text)
            
            # Convert to byte array
            byte_array = get_byte_array(padded_text)
            
            # Write compressed file
            self.file_handler.write_compressed_file(output_path, byte_array)
            
            # Save codes for decompression
            codes_path = output_path + ".codes"
            self.file_handler.save_codes(codes_path, codes)
            
            # Calculate and print statistics
            original_size = os.path.getsize(input_path)
            compressed_size = os.path.getsize(output_path)
            stats = calculate_compression_stats(original_size, compressed_size)
            
            self.cli.print_operation_complete("compression", output_path)
            self.cli.print_compression_stats(stats)
            
            return output_path
            
        except Exception as e:
            print(f"Error during compression: {e}")
            return None
    
    def decompress(self, input_path, output_path=None):
        """Decompress a file using Huffman coding"""
        try:
            # Set default output path if not provided
            if output_path is None:
                # Remove the .bin extension
                if input_path.endswith('.bin'):
                    output_path = input_path[:-4] + "_decompressed.txt"
                else:
                    output_path = input_path + "_decompressed.txt"
            
            # Load Huffman codes
            codes_path = input_path + ".codes"
            if not os.path.exists(codes_path):
                print("Codes file not found. Cannot decompress.")
                return None
                
            codes, reverse_mapping = self.file_handler.load_codes(codes_path)
            
            # Read compressed file
            byte_data = self.file_handler.read_compressed_file(input_path)
            
            # Convert bytes to bit string
            bit_string = get_bit_string(byte_data)
            
            # Remove padding
            encoded_text = HuffmanCore.remove_padding(bit_string)
            
            # Decode text
            decompressed_text = HuffmanCore.decode_text(encoded_text, reverse_mapping)
            
            # Write decompressed file
            self.file_handler.write_decompressed_file(output_path, decompressed_text)
            
            self.cli.print_operation_complete("decompression", output_path)
            
            return output_path
            
        except Exception as e:
            print(f"Error during decompression: {e}")
            return None
    
    def run(self):
        """Run the Huffman coding application"""
        self.cli.print_header()
        
        while True:
            self.cli.print_menu()
            choice = self.cli.get_choice()
            
            if choice == 1:  # Compress
                input_path = self.cli.get_input_path("compress")
                default_output = input_path + ".bin"
                output_path = self.cli.get_output_path(default_output)
                self.compress(input_path, output_path)
                
            elif choice == 2:  # Decompress
                input_path = self.cli.get_input_path("decompress")
                
                # Check if the codes file exists
                if not os.path.exists(input_path + ".codes"):
                    print("Codes file not found. Cannot decompress.")
                    continue
                
                # Set default output path
                if input_path.endswith('.bin'):
                    default_output = input_path[:-4] + "_decompressed.txt"
                else:
                    default_output = input_path + "_decompressed.txt"
                    
                output_path = self.cli.get_output_path(default_output)
                self.decompress(input_path, output_path)
                
            elif choice == 3:  # Exit
                print("\nExiting the application. Goodbye!")
                break

if __name__ == "__main__":
    huffman_app = HuffmanCoding()
    huffman_app.run()