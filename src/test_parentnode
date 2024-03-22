import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode

class TestParentNode(unittest.TestCase):
    def test_parent1(self):
        node = ParentNode(
            "a", 
            [
            LeafNode("b", "Bold"), 
            LeafNode(None, "Norm"), 
            LeafNode("a", "Link", {"href": "google.com"})
            ],
            )
        converted_node = node.to_html
        print(converted_node)
        expected = ""
        self.assertEqual(converted_node, expected)
        
if __name__ == "__main__":
    unittest.main()