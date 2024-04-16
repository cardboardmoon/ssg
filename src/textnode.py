class TextNode:
    def __init__(self, text, text_type, url=None, alt=None):
        self.text = text
        self.text_type = text_type
        self.url = url
        self.alt = alt

    def __eq__(self, other):
        return(
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type})" #, {self.url}, {self.alt})"

    def split_nodes_delimiter(old_nodes, delimiter, text_type):
        final_list = []
        plain_text = True
        for node in old_nodes:
            split_node = node.text.split(delimiter)
            for i in range(0, len(split_node)):
                if plain_text == True:
                    final_list.append(TextNode(split_node[i], "text"))
                    plain_text = False
                else: 
                    final_list.append(TextNode(split_node[i], text_type))
                    plain_text = True
        return final_list
