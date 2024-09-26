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
            f"HTMLNode({self.tag}," \
            f" {self.value}, {self.children}, {self.props})"
        )

