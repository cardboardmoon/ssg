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
    def __repr__(self):
        return f"tag:{self.tag} value:{self.value} children:{self.children} props:{self.props}"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props):
        super().__init__(tag, value, props=props)

    def to_html(self):
        print(self)
        if self.value == None: raise ValueError
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
    def __init__(self, tag, children, props):
        super().__init__(tag, children, props=props)

    def to_html(self):
        child_collection = ""
        if self.tag == None: raise ValueError
        if self.children == None: raise ValueError("The children are missing!")
        else:
            for child in self.children:
                child_collection += child.to_html
                child_collection += "\n"
            return f"<{self.tag}>\n{child_collection}\n</{self.tag}>"
