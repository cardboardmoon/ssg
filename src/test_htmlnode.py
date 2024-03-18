import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def prop_test1(self):
        expected_props = "href='https://google.com target='_blank'"
        node1 = HTMLNode(None, None, None, {"href": "https://google.com", "target": "_blank"})
        self.assertEqual(node1.props_to_html, expected_props)

if __name__ == "__main__":
    unittest.main()
