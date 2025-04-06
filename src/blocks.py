from enum import Enum



class BlockType(Enum):
    PARAGRAPH = 1
    HEADING = 2
    CODE = 3
    QOUTE = 4
    UNORDERED_LIST = 5
    ORDERED_LIST = 6

def block_to_block_type(markdown_block):
    block_lines = markdown_block.split("\n")
    print(block_lines)
    match block_lines[0][0]:
        case '#':
            for i in range(len(block_lines[0])):
                if i > 6:
                    return BlockType.PARAGRAPH
                if block_lines[0][i] != '#':
                    if block_lines[0][i] == ' ':
                        return BlockType.HEADING
        case "`":
            if block_lines[0][:3] == "```" and block_lines[-1][-3:] == "```":
                return BlockType.CODE
            else:
                return BlockType.PARAGRAPH
        case ">":
            for i in range(len(block_lines)):
                if block_lines[i][0] != ">":
                    break
                if i == (len(block_lines)-1):
                    return BlockType.QOUTE
            return BlockType.PARAGRAPH
        case "-":
            for i in range(len(block_lines)):
                if block_lines[i][:2] != "- ":
                    break
                if i == (len(block_lines)-1):
                    return BlockType.UNORDERED_LIST
            return BlockType.PARAGRAPH
        case "1":
            for i in range(len(block_lines)):
                line_split = block_lines[i].split(' ')
                if line_split[0] != f"{i + 1}.":
                    break
                if i == (len(block_lines)-1):
                        return BlockType.ORDERED_LIST
            return BlockType.PARAGRAPH
        case _:
            return BlockType.PARAGRAPH