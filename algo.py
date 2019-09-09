from Node import Node
import numpy as np
import itertools
from GUI import main_gui
import xlwt as excel

def check_type(node):
	if node.is_mendatory:
		return 1
	elif node.is_alternative:
		return 2
	elif node.is_or:
		return 3
	else:
		return 4


def multiply_solutions(arr1, arr):

	if arr1:
		for a in arr1:
			if a == 0:
				if type(arr[0]) is list:
					arr.append([0]*len(arr[0]))
				else:
					arr.append([0] * len(arr))
	return arr

def group_combi(group_root, PCR, solution_array,n):

	if group_root.children == None:
		if PCR == 1:
			possible = multiply_solutions(solution_array, [1])

			return possible
		if PCR == 2:
			possible = [1]*len(group_root.parent.children)
			possible = np.array(possible)
			possible = np.diag(possible)
			possible = possible.tolist()
			possible = multiply_solutions(solution_array, possible)
			return possible
		elif PCR == 3:
			possible = [1] * len(group_root.parent.children)
			possible = np.array(possible)
			possible = np.diag(possible)
			possible = possible.tolist()
			possible.append(([1] * len(group_root.parent.children)))
			possible = multiply_solutions(solution_array, possible)
			return possible

		elif PCR == 4:
			possible = multiply_solutions(solution_array, [0,1])
			return possible
	else:
		if PCR == 1:
			possible = multiply_solutions(solution_array, [1])
			return group_combi(group_root.children[n], check_type(group_root.children[n]), possible, 0)
		if PCR == 2:
			possible = [1]*len(group_root.children)

			possible = np.array(possible)
			possible = np.diag(possible)
			possible = possible.tolist()
			possible = multiply_solutions(solution_array, possible)
			return group_combi(group_root.children[n], check_type(group_root.children[n]), possible, 0)
		if PCR == 3:
			possible = [1]*len(group_root.children)
			possible = np.array(possible)
			possible = np.diag(possible)
			possible = possible.tolist()
			possible.append(([1]*len(group_root.children)))
			possible = multiply_solutions(solution_array, possible)
			return group_combi(group_root.children[0], check_type(group_root.children[n]), possible, 0)
		elif PCR == 4:
			possible = multiply_solutions(solution_array,[0,1])
			return group_combi(group_root.children[0], check_type(group_root.children[n]), possible, 0)


def product_combination(root, leaf_nodes):
	group_products = []
	for child in root.children:
		group_products.append(group_combi(child, check_type(child), None, 0))
	keys = leaf_nodes.keys()
	index = 0
	for t in itertools.product(*group_products):
		for tt in range(len(t)):
			if type(t[tt]) is list or type(t[tt]) is tuple:
				for ttt in range(0,len(t[tt])):
					leaf_nodes[list(keys)[index]].append(t[tt][ttt])
					index+=1
			else:
				leaf_nodes[list(keys)[index]].append(t[tt])
				index+=1
		index = 0
	return leaf_nodes

def root(node_dict):
	for node in node_dict.values():
		if node.parent == None:
			return node


def leaf_nodes(node_dict):
	leaf_node_dict = dict()
	for k in node_dict.keys():
		temp_node = node_dict.get(k)
		if temp_node.children is None:
			key = temp_node.name
			leaf_node_dict[key] = []
	return leaf_node_dict

def file_read():
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
						node.is_alternative =  True
			elif line_parts[0] == "OR":
				line_parts[1] = (line_parts[1][:-1])
				OR_array = line_parts[1].split(',')
				for item in OR_array:
					node = node_dict.get(item)
					if node is not None:
						node.is_or =  True

			elif line_parts[0] == "PC":
				line_parts[1] = (line_parts[1][:-1])

				sub_line_parts = line_parts[1].split(';')
				for item in sub_line_parts:
					parent_child = item.split(':')
					child_names_array_= parent_child[1].split(',')
					child_node_array = []
					for na in child_names_array_:
						temp = node_dict.get(na)
						if temp:
							temp.parent = node_dict.get(parent_child[0])
							child_node_array.append(temp)
					node_dict[parent_child[0]].children = child_node_array

		return node_dict
def remove_combinations_from_dict(combinations,index_array):
	turn = 0
	for i in index_array:
		for k in combinations.keys():
			del combinations.get(k)[i-turn]

		turn += 1
	return combinations

def get_combination():
	node_dict = file_read()

	inclusive_exclusive_dict = main_gui(list(leaf_nodes(node_dict).keys()))
	total_combinations =  product_combination(root(node_dict), leaf_nodes(node_dict))
	to_remove_index_list = []
	for k in inclusive_exclusive_dict.get('inclusive').keys():
		inclusive_to = inclusive_exclusive_dict.get('inclusive').get(k)
		count=0
		combo=total_combinations.get(k)
		combo1 = total_combinations.get(inclusive_to)
		for i in range(len(combo)):
			if combo[i] is 1 and combo1[i] is 0:
				to_remove_index_list.append(count)
			count += 1

	total_combinations_after_inclusive = remove_combinations_from_dict(total_combinations,to_remove_index_list)
	to_remove_index_list_exclusive = []
	for k in inclusive_exclusive_dict.get('exclusive').keys():
		exclusive_to = inclusive_exclusive_dict.get('exclusive').get(k)
		count = 0
		combo = total_combinations_after_inclusive.get(k)
		combo1 = total_combinations_after_inclusive.get(exclusive_to)

		for i in range(len(combo)):
			if combo[i] is 1 and combo1[i] is 1:
				to_remove_index_list_exclusive.append(count)
			count += 1

	total_combinations_after_exclusive = remove_combinations_from_dict(
		total_combinations_after_inclusive, to_remove_index_list_exclusive)
	return total_combinations_after_exclusive


result = get_combination()
if result is not None:
	file = excel.Workbook()
	sheet = file.add_sheet('output',True)
	column = 1
	row = 1
	for k in result.keys():

		sheet.write(0,column,k)

		for element in result.get(k):
			sheet.write(row, column, element)
			row+=1
		row = 1
		column += 1
	file.save('output.xlsx')
