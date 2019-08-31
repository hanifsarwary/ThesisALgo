class Node:
    
    def __init__(self, name, parent=None, children=None, is_mendatory=None, is_alternative=None, is_or=None):
        self.name = name
        self.parent = parent
        self.children = children
        self.is_mendatory = is_mendatory
        self.is_alternative = is_alternative
        self.is_or = is_or

    def __str__(self):
        stri = self.name +" child of " + self.parent.name
        if self.is_mendatory:
            stri+= " it is mandetory"
        elif self.is_alternative:
            stri += " it is alternative"
        elif self.is_or:
            stri += " it is or"
        return stri