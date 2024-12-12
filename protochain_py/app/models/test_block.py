import unittest
from block import Block

class TestBlock(unittest.TestCase):
    def setUp(self) -> None:
        self.block  = Block(1, "ABC")
        self.block_without_index  = Block(-1, "ABC")
        self.block_without_hash  = Block(1, "")
        
    def test_is_valid(self):
        self.assertTrue(self.block.is_valid())
    
    def test_is_valid_index(self):
        self.assertFalse(self.block_without_index.is_valid())
        
    def test_is_valid_hash(self):
        self.assertFalse(self.block_without_hash.is_valid())
        
    
    
if __name__ == '__main__':
    unittest.main()