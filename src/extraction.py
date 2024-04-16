import re
import TextNode

test_text1 = "MKDOWN image test ![image](https://google.com) and here's ![another](https://cnn.com)"
test_text2 = "MKDOWN link test [link](https://google.com) and here's [another](https://cnn.com)"
test_node1 = TextNode(test_text1, "text")
test_node2 = TextNode(test_text2, "text")

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)

def split_nodes_image(old_nodes):
    final_list = []
    for node in old_nodes:
        images = extract_markdown_images(node.text)
    for tup in images:
        final_list.append(TextNode(tup[0]))
    return final_list

#def split_nodes_links(old_nodes):