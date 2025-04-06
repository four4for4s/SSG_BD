from textnode import TextNode, TextType


class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        html_str = ""
        if self.props != None:
            for key, value in self.props.items():
                html_str += f'{key}="{value}" '
        return html_str[:-1]
        
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def __eq__(self, obj2):
        return (self.tag == obj2.tag and self.value == obj2.value and self.children == obj2.children and self.props == self.props)

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError
        
        if self.tag == None:
            return self.value


        return (f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>")
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("needs tag")
        
        if self.children is None:
            raise ValueError("needs children")

        return (f"<{self.tag}>{''.join(map(lambda x: x.to_html(), self.children))}</{self.tag}>")

def text_node_to_html_node(text_node):
        if text_node.text_type == TextType.TEXT:
            return LeafNode(None, text_node.text)

        if text_node.text_type == TextType.BOLD:
            return LeafNode("b", text_node.text)

        if text_node.text_type == TextType.ITALIC:
            return LeafNode("i", text_node.text)

        if text_node.text_type == TextType.CODE:
            return LeafNode("code", text_node.text)

        if text_node.text_type == TextType.LINK:
            return LeafNode("a", text_node.text, {"href":stext_nodeelf.url})

        if text_node.text_type == TextType.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})