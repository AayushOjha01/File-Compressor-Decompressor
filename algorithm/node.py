class HuffmanNode:
    """Node class for Huffman tree"""
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        """For comparison in priority queue"""
        return self.freq < other.freq
    
    def __eq__(self, other):
        """For equality comparison"""
        if not isinstance(other, HuffmanNode):
            return False
        return self.freq == other.freq and self.char == other.char
    