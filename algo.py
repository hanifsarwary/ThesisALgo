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

def root(node_dict):
	for node in node_dict.values():
		if node.parent_name == None:
			print("I'm root node")
			return node
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
					node.is_mendatory =  True

		elif line_parts[0] == "Alternative":
			line_parts[1] = (line_parts[1][:-1])
			Alternative = line_parts[1].split(',')
			#print(Alternative)
			for item in Alternative:
				node = node_dict.get(item)
				if node is not None:
					node.set_is_alternative =  True
		elif line_parts[0] == "OR":
			line_parts[1] = (line_parts[1][:-1])
			OR_array = line_parts[1].split(',')
			#print(OR_array)
			for item in OR_array:
				node = node_dict.get(item)
				if node is not None:
					node.set_is_or =  True
		elif line_parts[0] == "inclusive":
			line_parts[1] = (line_parts[1][:-1])
			try:
				sub_line_parts = line_parts[1].split(':')
				for part in sub_line_parts:
					sub_line_parts = part.split(',')
					inclusive.append(sub_line_parts)
				for items in inclusive:
					node0 = node_dict.get(items[0])
					if node0 is not None:
						node0.inclusive_to = items[1]
					node1 = node_dict.get(items[1])
					if node1 is not None:
						node1.inclusive_to = items[0]
			except:
				inclusive = line_parts[1].split(',')
				node0 = node_dict.get(inclusive[0])
				if node0 is not None:
					node0.inclusive_to(inclusive[1])
				node1 = node_dict.get(inclusive[1])
				if node1 is not None:
					node1.inclusive_to(inclusive[0])
			#print(inclusive)
		elif line_parts[0] == "exclusive":
			line_parts[1] = (line_parts[1][:-1])
			try:
				sub_line_parts = line_parts[1].split(':')
				for part in sub_line_parts:
					sub_line_parts = part.split(',')
					exclusive.append(sub_line_parts)
				for items in exclusive:
					node0 = node_dict.get (items[0])
					if node0 is not None:
						node0.exclusive_to = items[1]
					node1 = node_dict.get(items[1])
					if node1 is not None:
						node1.exclusive_to = items[0]
			except:
				exclusive = line_parts[1].split(',')
				node0 = node_dict.get(exclusive[0])
				if node0 is not None:
					node0.exclusive_to(exclusive[1])
				node1 = node_dict.get(exclusive[1])
				if node1 is not None:
					node1.exclusive_to = exclusive[0]
			#print(exclusive)
		elif line_parts[0] == "PC":
			line_parts[1] = (line_parts[1][:-1])
			try:
				sub_line_parts = line_parts[1].split(';')
				for item in sub_line_parts:
					parent_child = item.split(':')
					PC[parent_child[0]] = parent_child[1].split(',')
				for name in FeatureNames:
					for key in PC.keys():
						if name in PC[key]:
							parent_node = node_dict.get(name)
							if parent_node is not None:
								parent_node.parent_name = key
						child_node = node_dict.get(key)
						if child_node is not None:
							child_node.children = PC[key]
				"""
				for keys in PC.keys():
					for key in PC.keys():
						if keys in PC[key]:
							#print(keys + ' My parent is ' + key)
							parent_node = node_dict.get(keys)
							if parent_node is not None:
								parent_node.parent_name = key
						child_node = node_dict.get(key)
						if child_node is not None:
							child_node.children = PC[key]
				"""
			except:
				parent_child = line_parts[1].split(':')
				PC[parent_child[0]] = parent_child[1].split(',')
			test_root = root(node_dict)
			print(test_root.name,test_root.children)



