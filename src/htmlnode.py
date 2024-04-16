from textnode import TextNode

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        props_list = []
        for key, val in self.props.items():
            props_list.append(f" {key}='{val}'")
        return "".join(props_list)
    
    def text_node_to_html_node(text_node):
        match text_node.text_type:
            case "text":
                return LeafNode(None, text_node.text, None)
            case "bold":
                return LeafNode("b", text_node.text, None)
            case "italic":
                return LeafNode("i", text_node.text, None)
            case "code":
                return LeafNode("code", text_node.text, None)
            case "link":
                return LeafNode("a", text_node.text, {"href": text_node.url})
            case "image":
                return LeafNode("img", "", {"src": text_node.url, "alt": text_node.alt})
            case other:
                raise Exception("Text Node type is not valid.")

    def __repr__(self):
        return f"tag:{self.tag} value:{self.value} children:{self.children} props:{self.props}"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props):
        super().__init__(tag, value, props=props)

    def to_html(self):
        #print(self)
        if self.value == None: raise ValueError("No value!")
        if self.tag == None: return str(self.value)
        else:
            # With link
            if self.props != None:
                for key, value in self.props.items():
                    return f"<a {key.strip("'")}={value}>{self.value}</a>"
            # No link
            else:
                return f"<{self.tag}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children):
        super().__init__(tag=tag, children=children)

    def to_html(self):
        child_collection = ""
        if self.tag == None: raise ValueError("No tag!")
        if self.children == None: raise ValueError("The children are missing!")
        else:
            for child in self.children:
                child_collection += child.to_html()
                #child_collection += "\n"
            return f"<{self.tag}>{child_collection}</{self.tag}>"
