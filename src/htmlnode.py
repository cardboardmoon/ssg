class HTMLNode:
    def __init__(tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementedError
    def props_to_html(self):
        props_list = []
        for key, val in self.props:
            props_list.append(f" {key}='{val}'")
        return "".join(props_list)
    def __repr__(self):
        return f"tag:{self.tag} value:{self.value} children:{self.children} props:{self.props}"