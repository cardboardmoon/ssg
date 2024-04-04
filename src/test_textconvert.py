import unittest

from textnode import TextNode
from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode

class TestTextNode(unittest.TestCase):
    # plain_test = TextNode("plain", "text")
    # bold_test = TextNode("boldsies", "bold")
    # italic_test = TextNode("italicsies", "italic")
    # code_test = TextNode("beep boop", "code")
    # link_test = TextNode("website", "link", "www.notarealsite.com")
    # image_test = TextNode("", "image", "https://upload.wikimedia.org/wikipedia/commons/thumb/7/71/2010-kodiak-bear-1.jpg/1200px-2010-kodiak-bear-1.jpg", "a brown bear")
    # error_test = TextNode("fake", "butt")
    # def test_convert1(self):
    #     print(HTMLNode.text_node_to_html_node(self.plain_test))
    #     print(HTMLNode.text_node_to_html_node(self.bold_test))
    #     print(HTMLNode.text_node_to_html_node(self.italic_test))
    #     print(HTMLNode.text_node_to_html_node(self.code_test))
    #     print(HTMLNode.text_node_to_html_node(self.link_test))
    #     print(HTMLNode.text_node_to_html_node(self.image_test))
    #     print(HTMLNode.text_node_to_html_node(self.error_test))

    def test_convert2(self):
        node = TextNode("The penultimate word is **bold** right?", "text")
        new_nodes = HTMLNode.split_nodes_delimiter(node, "**", "bold")
        expected = [TextNode("The penultimate word is ", "text",), TextNode("bold", "bold"), TextNode(" right?", "text")]
        return self.assertEqual(new_nodes, expected)

if __name__ == "__main__":
    unittest.main()
