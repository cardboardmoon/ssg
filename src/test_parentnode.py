# import unittest

# from htmlnode import HTMLNode
# from htmlnode import LeafNode
# from htmlnode import ParentNode

# class TestParentNode(unittest.TestCase):
#     def test_parent1(self):
#         # Easy test
#         node = ParentNode(
#                 "p",
#                 [
#                     LeafNode("b", "Bold", None), 
#                     LeafNode(None, "Norm", None), 
#                     LeafNode("a", "Link", {"href": "google.com"})
#                 ]
#             )
#         converted_node = node.to_html()
#         expected = "<p><b>Bold</b>Norm<a href=google.com>Link</a></p>"
#         print(f"expected: {expected}")
#         print(f"actual:   {converted_node}")
#         self.assertEqual(converted_node, expected)
    
#     def test_parent2(self):
#         # Nested test
#         node = ParentNode(
#                 "p", 
#                 [
#                     LeafNode("i", "Italic", None), 
#                     ParentNode(
#                         "i",
#                         [
#                             LeafNode("a", "booty site", {"href": "www.booty.com"}),
#                             LeafNode("b", "Emboldened", None)
#                         ]
#                     )
#                 ]
#             )
#         converted_node = node.to_html()
#         expected = "<p><i>Italic</i><i><a href=www.booty.com>booty site</a><b>Emboldened</b></i></p>"
#         print(f"expected: {expected}")
#         print(f"actual:   {converted_node}")
#         self.assertEqual(converted_node, expected)

#     def test_parent3(self):
#         # Error test
#         node = ParentNode(
#                 "a",
#                 [
#                     LeafNode("b", None, None),
#                     LeafNode("a", "Link", {"href": "google.com"})
#                 ]
#             )
#         converted_node = node.to_html()
#         expected = ""
#         print(f"expected: {expected}")
#         print(f"actual:   {converted_node}")
#         self.assertEqual(converted_node, expected)

# if __name__ == "__main__":
#     unittest.main()