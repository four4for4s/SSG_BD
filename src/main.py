from textnode import *
from htmlnode import *
from textops import *
from blocks import *

def main():
    block2 = """>this is
>a quote
dd
> another quote with a space"""

    blocktype1 = block_to_block_type(block2)
    print(blocktype1)
if __name__ == "__main__":
    main()