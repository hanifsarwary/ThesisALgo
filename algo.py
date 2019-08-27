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
	
	def set_children(self, child_array):
    		self.children = child_array
	
	def set_is_mandetory(self, is_mendatory):
    		self.is_mendatory = is_mendatory
	
	def set_is_alternative(self, is_alternative):
    		self.is_alternative = is_alternative
	
	def set_is_or(self, is_or):
    		self.is_or = is_or
	
	#### baqi setter bna lai python ma zaroorat ni hoti pr clarity k liye acha hota ha
	####


with open("input.txt", "r") as file:
	FeatureNames = []
	Mendatory = []
	Alternative = []
	OR_array = []
	inclusive = []
	exclusive = []
	PC = dict()
	sub_line_parts = []
	node_dict = dict()
	for line in file:
		line_parts = line.split('->')
		if line_parts[0] == "Feature Names":
			line_parts[1] = (line_parts[1][:-1])
			FeatureNames =  line_parts[1].split(',')
			
			for f_name in FeatureNames:
    			node_temp = Node(name=f_name)
				node_dict[f_name] = node_temp

		elif line_parts[0] == "Mendatory":
			line_parts[1] = (line_parts[1][:-1])
			Mendatory = line_parts[1].split(',')
			for men in Mendatory:
    			node = node_dict.get(men)
				if node is not None:
    				node.set_is_mandetory(True)
			
		elif line_parts[0] == "Alternative":
			line_parts[1] = (line_parts[1][:-1])
			try:
				sub_line_parts = line_parts[1].split(':')
				for part in sub_line_parts:
					sub_line_parts = part.split(',')
					Alternative.append(sub_line_parts)
			except:
				Alternative = line_parts[1].split(',')
			print(Alternative)
		elif line_parts[0] == "OR":
			line_parts[1] = (line_parts[1][:-1])
			try:
				sub_line_parts = line_parts[1].split(':')
				for part in sub_line_parts:
					sub_line_parts = part.split(',')
					OR_array.append(sub_line_parts)
			except:
				OR_array = line_parts[1].split(',')
			print(OR_array)
		elif line_parts[0] == "inclusive":
			line_parts[1] = (line_parts[1][:-1])
			try:
				sub_line_parts = line_parts[1].split(':')
				for part in sub_line_parts:
					sub_line_parts = part.split(',')
					inclusive.append(sub_line_parts)
			except:
				inclusive = line_parts[1].split(',')
			print(inclusive)
		elif line_parts[0] == "exclusive":
			line_parts[1] = (line_parts[1][:-1])
			try:
				sub_line_parts = line_parts[1].split(':')
				for part in sub_line_parts:
					sub_line_parts = part.split(',')
					exclusive.append(sub_line_parts)
			except:
				exclusive = line_parts[1].split(',')
			print(exclusive)
		elif line_parts[0] == "PC":
			line_parts[1] = (line_parts[1][:-1])
			try:
				sub_line_parts = line_parts[1].split(';')
				for item in sub_line_parts:
					parent_child = item.split(':')
					PC[parent_child[0]] = parent_child[1].split(',')
			except:
				parent_child = line_parts[1].split(':')
				PC[parent_child[0]] = parent_child[1].split(',')
			print(PC)

