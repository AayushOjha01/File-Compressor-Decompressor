from collections import Counter
from .node import HuffmanNode
from .min_heap import MinHeap

class HuffmanCore:
    """Core algorithms for Huffman encoding and decoding"""

    @staticmethod
    def build_frequency_table(text):
        """Create frequency dictionary for each character in text"""
        return Counter(text)
    
    @staticmethod
    def build_huffman_tree(frequency_table):
        """Build a huffman tree from the frequency table and return the root node"""
        min_heap = MinHeap()

        for char, freq in frequency_table.items():
            min_heap.push(HuffmanNode(char, freq))
        
        # Build huffman tree: combine the two lowest frequency nodes until there is only one node left.
        while len(min_heap) > 1:
            left = min_heap.pop()
            right = min_heap.pop()

            # Create internal node with these two nodes as children and frequency equal to sum of nodes' freq
            internal_node = HuffmanNode(None, left.freq + right.freq)
            internal_node.left = left
            internal_node.right = right

            min_heap.push(internal_node)
        
        return min_heap.pop() if not min_heap.is_empty() else None
    
    @staticmethod
    def generate_codes(root):
        """Generate huffman codes for each char in the tree"""
        codes = {}
        reverse_mapping = {}

        def _traverse(node, current_code):
            if node is None:
                return
            
            if node.char is not None:
                codes[node.char] = current_code
                reverse_mapping[current_code] = node.char
            
            # traverse left with '0' and right with '1'
            _traverse(node.left, current_code + "0")
            _traverse(node.right, current_code + "1")

        _traverse(root, "")
        return codes, reverse_mapping
    
    @staticmethod
    def encode_text(text, codes):
        """Convert text to binary string using Huffman codes"""
        return ''.join(codes[char] for char in text)

    @staticmethod
    def pad_encoded_text(encoded_text):
        """Add padding to make encoded text a multiple of 8 bits"""
        padding = 8 - (len(encoded_text) % 8)
        if padding == 8:
            padding = 0
        
        # First byte stores the padding information
        padded_info = "{0:08b}".format(padding)
        padded_text = padded_info + encoded_text + "0" * padding
        return padded_text
    
    @staticmethod
    def remove_padding(padded_text):
        """Remove padding from the padded encoded text"""
        # First byte contains the padding information
        padded_info = padded_text[:8]
        padding = int(padded_info, 2)
        
        # Remove padding information and actual padding
        bit_string = padded_text[8:-padding] if padding > 0 else padded_text[8:]
        return bit_string
    
    @staticmethod
    def decode_text(encoded_text, reverse_mapping):
        """Decode Huffman encoded text to original text"""
        decoded_text = ""
        current_code = ""
        
        for bit in encoded_text:
            current_code += bit
            if current_code in reverse_mapping:
                decoded_text += reverse_mapping[current_code]
                current_code = ""
                
        return decoded_text