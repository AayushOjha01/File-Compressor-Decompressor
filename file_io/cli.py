import os

class CLI:
    """Command Line Interface for Huffman coding application"""
    
    @staticmethod
    def print_header():
        """Print application header"""
        print("\n" + "="*50)
        print("      HUFFMAN CODING FILE COMPRESSION")
        print("="*50)
    
    @staticmethod
    def print_menu():
        """Print main menu options"""
        print("\nOptions:")
        print("  1. Compress a file")
        print("  2. Decompress a file")
        print("  3. Exit")
    
    @staticmethod
    def get_choice():
        """Get user choice from menu"""
        while True:
            try:
                choice = input("\nEnter your choice (1-3): ")
                choice = int(choice)
                if 1 <= choice <= 3:
                    return choice
                else:
                    print("Invalid choice. Please enter a number between 1 and 3.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    @staticmethod
    def get_input_path(operation_type):
        """Get and validate input file path"""
        while True:
            input_path = input(f"Enter the path of the file to {operation_type}: ")
            if os.path.exists(input_path) and os.path.isfile(input_path):
                return input_path
            else:
                print(f"File does not exist. Please enter a valid file path.")
    
    @staticmethod
    def get_output_path(default_path):
        """Get output file path or use default"""
        output_path = input(f"Enter the output path (leave blank for {default_path}): ")
        return output_path if output_path else default_path
    
    @staticmethod
    def print_compression_stats(stats):
        """Print compression statistics"""
        print("\nCompression Statistics:")
        print(f"  Original size: {stats['original_size']} bytes")
        print(f"  Compressed size: {stats['compressed_size']} bytes")
        print(f"  Compression ratio: {stats['compression_ratio']}%")
        print(f"  Space saving: {stats['space_saving']}%")
    
    @staticmethod
    def print_operation_complete(operation_type, output_path):
        """Print operation completion message"""
        print(f"\n{operation_type.capitalize()} completed successfully!")
        print(f"Output saved to: {output_path}")