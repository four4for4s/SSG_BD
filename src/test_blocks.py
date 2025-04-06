import unittest

from blocks import *


class TestHtmlNode(unittest.TestCase):

    def test_blocktype(self):
        block1 = "# this is a heading"
        block2 = """```this is a block of code
more code
this is the end of the code```"""
        block3 = """>this is
>a quote
> another quote with a space"""
        block4 = """- this is
- an
- unordered list"""
        block5 = """1. first
2. second
3. third"""
        blocktype1 = block_to_block_type(block1)
        blocktype2 = block_to_block_type(block2)
        blocktype3 = block_to_block_type(block3)
        blocktype4 = block_to_block_type(block4)
        blocktype5 = block_to_block_type(block5)
        self.assertEqual(blocktype1, BlockType.HEADING)
        self.assertEqual(blocktype2, BlockType.CODE)
        self.assertEqual(blocktype3, BlockType.QOUTE)
        self.assertEqual(blocktype4, BlockType.UNORDERED_LIST)
        self.assertEqual(blocktype5, BlockType.ORDERED_LIST)


if __name__ == "__main__":
    unittest.main()