class Node:
    
    def __init__(self, name, parent_name=None, children=None, is_mendatory=None, is_alternative=None, is_or=None, inclusive_to=None, exclusive_to=None):
        self.name = name
        self.parent_name = parent_name
        self.children = children
        self.is_mendatory = is_mendatory
        self.is_alternative = is_alternative
        self.is_or = is_or
        self.inclusive_to = inclusive_to
        self.exclusive_to = exclusive_to

    def set_parent(self, p_name):
        self.parent_name = p_name