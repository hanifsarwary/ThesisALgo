from Node import Node
import numpy as np

def check_type(node):
	if node.is_mendatory == True:
		return 1
	elif node.is_alternative == True:
		return 2
	elif node.is_or == True:	
		return 3
	else:
		return 4


def multiply_solutions(arr1, arr):

	if arr1:
		for a in arr1:
			if type(a) is list:
				for i in a:
					if i == 0:
						arr.append([0] * len(arr[0]))
	return arr


def group_combi(group_root, PCR, solution_array,n):
	
	if group_root.children == None:
		if PCR == 2:
			possible = [1]*len(group_root.children)
			possible = np.array(possible)
			possible = np.diag(possible)
			possible = multiply_solutions(possible, solution_array)
			return possible
		elif PCR == 3:
			possible = [1] * len(group_root.children)
			possible = np.array(possible)
			possible = np.diag(possible)
			possible.append(np.array([1] * len(group_root.children)))
			possible = multiply_solutions(possible, solution_array)
			return possible

		elif PCR == 4:
			possible = multiply_solutions([0,1], solution_array)
			return possible
	else:
		if PCR == 2:
			possible = [1]*len(group_root.children)
			possible = np.array(possible)
			possible = np.diag(possible)
			possible = multiply_solutions(possible, solution_array)
			group_combi(group_root, check_type(group_root), possible, 0)
		if PCR == 3:
				possible = [1]*len(group_root.children)
				possible = np.array(possible)
				possible = np.diag(possible)
				possible.append(np.array([1]*len(group_root.children)))
				possible = multiply_solutions(possible, solution_array)
				group_combi(group_root, check_type(group_root), possible, 0)
		elif PCR == 4:
			possible = multiply_solutions([0,1], solution_array)
			group_combi(group_root, check_type(group_root), possible, 0)


def  product_combination(root):
	group_products = []
	for child in root.children:
		group_products.append(group_combi(child, check_type(child), None, 0))


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
			for item in Alternative:
				node = node_dict.get(item)
				if node is not None:
					node.set_is_alternative =  True
		elif line_parts[0] == "OR":
			line_parts[1] = (line_parts[1][:-1])
			OR_array = line_parts[1].split(',')
			for item in OR_array:
				node = node_dict.get(item)
				if node is not None:
					node.set_is_or =  True

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
			except:
				parent_child = line_parts[1].split(':')
				PC[parent_child[0]] = parent_child[1].split(',')
			test_root = root(node_dict)
			print(test_root.name,test_root.children)



