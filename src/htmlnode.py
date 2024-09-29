class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        props_converted = ""
        for k, v in self.props.items():
            props_converted += f" {k}='{v}'"
        return props_converted
        
    def __eq__(self, other):
        if (
            self.tag == other.tag and self.value == other.value
        and self.children == other.children and self.props == other.props
        ):
            return True
        
    def __repr__(self):
        return (
            f"HTMLNode({self.tag},"
            f" {self.value}, {self.children}, {self.props})"
        )

class ParentNode(HTMLNode):
    def __init__(self, children, tag=None, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("There is no tag present.")
        if not self.children:
            raise ValueError("There are no children present.")
        result = ""
        for child in self.children:
            result += child.to_html()
        props_string = HTMLNode.props_to_html(self) if self.props else ""
        return f"<{self.tag}{props_string}>{result}</{self.tag}>"

class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        super().__init__(tag, value, None, props )

    def to_html(self):
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return f"{self.value}"
        props_string = HTMLNode.props_to_html(self) if self.props else ""
        return (
            f"<{self.tag}{props_string}>"
            f"{self.value}</{self.tag}>"
        )