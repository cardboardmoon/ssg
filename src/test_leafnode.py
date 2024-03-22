# import unittest

# from htmlnode import HTMLNode
# from htmlnode import LeafNode

# class TestLeafNode(unittest.TestCase):
#     def test_leaf1(self):
#         node = LeafNode("a", "Clixxx", {"href": "https://google.com"})
#         converted_node = node.to_html()
#         expected = "<a href=https://google.com>Clixxx</a>"
#         print(f"expected: {expected}")
#         print(f"converted: {converted_node}")
#         print("===================================")
#         self.assertEqual(converted_node, expected)

#     def test_leaf2(self):
#         node = LeafNode("p", "Paragraph", None)
#         converted_node = node.to_html()
#         expected = "<p>Paragraph</p>"
#         print(f"expected: {expected}")
#         print(f"converted: {converted_node}")
#         print("===================================")
#         self.assertEqual(converted_node, expected)
        
#     def test_leaf3(self):
#         node = LeafNode(None, "raw raw", None)
#         converted_node = node.to_html()
#         expected = "raw raw"
#         print(f"expected: {expected}")
#         print(f"converted: {converted_node}")
#         print("===================================")
#         self.assertEqual(converted_node, expected)

# if __name__ == "__main__":
#     unittest.main()
